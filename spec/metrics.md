# OpenAIX Metrics Specification
## 四大评分维度算法详解

本文档面向开发者和架构师，详细说明 OpenAIX 评分的计算方法和实现细节。

---

## 1. SNR（信噪比）算法

### 1.1 算法流程

```python
def calculate_snr(html: str) -> SNRResult:
    # Step 1: 计算原始 Token 数
    raw_tokens = count_tokens(html)
    
    # Step 2: 清理 HTML
    soup = BeautifulSoup(html, 'lxml')
    for tag in ['script', 'style', 'noscript', 'iframe', 
                'canvas', 'svg', 'template', 'embed', 'object']:
        for element in soup.find_all(tag):
            element.decompose()
    
    # Step 3: 转换为 Markdown
    clean_html = str(soup)
    markdown = markdownify(clean_html)
    
    # Step 4: 计算清理后 Token 数
    clean_tokens = count_tokens(markdown)
    
    # Step 5: 计算 SNR
    snr = (clean_tokens / raw_tokens) * 100 if raw_tokens > 0 else 0
    
    # Step 6: 转换为分数
    score = snr_to_score(snr)
    
    return SNRResult(
        score=score,
        snr_percent=snr,
        raw_tokens=raw_tokens,
        clean_tokens=clean_tokens
    )
```

### 1.2 Token 计数器

使用 `tiktoken` 库，采用 `cl100k_base` 编码：

```python
import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")
tokens = encoder.encode(text)
count = len(tokens)
```

### 1.3 分数映射函数

```python
def snr_to_score(snr: float) -> int:
    if snr >= 40:
        return 100
    elif snr >= 20:
        # 线性插值: 20% -> 70, 40% -> 100
        return int(70 + (snr - 20) * 1.5)
    elif snr >= 10:
        # 线性插值: 10% -> 50, 20% -> 70
        return int(50 + (snr - 10) * 2)
    elif snr >= 5:
        # 线性插值: 5% -> 30, 10% -> 50
        return int(30 + (snr - 5) * 4)
    else:
        # < 5%: 线性递减
        return max(0, int(snr * 6))
```

### 1.4 实际案例

| 网站 | Raw Tokens | Clean Tokens | SNR | Score |
|------|-----------|--------------|-----|-------|
| docs.python.org | 15,000 | 13,800 | 92% | 100 |
| github.com | 45,000 | 5,400 | 12% | 54 |
| stripe.com/docs | 38,000 | 1,140 | 3% | 18 |

---

## 2. Semantic Structure 算法

### 2.1 总分构成

```
Semantic Score = 
    semantic_tags(25) + 
    headings(25) + 
    json_ld(25) + 
    images(10) + 
    metadata(15)
```

### 2.2 语义标签检测

```python
SEMANTIC_TAGS = ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']

used_tags = [tag for tag in SEMANTIC_TAGS if soup.find(tag)]
score = (len(used_tags) / 7) * 25
```

### 2.3 JSON-LD 质量评估

```python
def analyze_json_ld(scripts: List[Tag]) -> int:
    if not scripts:
        return 0
    
    max_score = 0
    for script in scripts:
        try:
            data = json.loads(script.string)
            score = 0
            
            # 基础分
            if '@context' in data:
                score += 5
            if '@type' in data:
                score += 5
            
            # 内容质量
            important_fields = ['name', 'description', 'url', 
                              'author', 'datePublished', 'image']
            if any(f in data for f in important_fields):
                score += 5
            
            # 丰富度
            if len(script.string) > 500:
                score += 10
            
            max_score = max(max_score, score)
        except:
            continue
    
    return min(25, max_score)
```

### 2.4 Hidden Gem 检测

```python
def is_hidden_gem(soup: BeautifulSoup, snr: float, json_ld_score: int) -> bool:
    # 计算文本密度
    text = soup.get_text(strip=True)
    html_str = str(soup)
    text_density = len(text) / len(html_str) if html_str else 1
    
    # 检测条件
    return (
        text_density < 0.15 and           # 视觉丰富
        json_ld_score >= 15 and            # 结构化数据好
        bool(soup.find('h1')) and          # 基本内容质量
        snr < 40                           # 低 SNR（视觉复杂）
    )
```

---

## 3. Token Economy 算法

### 3.1 简单的阶梯评分

```python
def calculate_token_economy(clean_tokens: int) -> TokenResult:
    if clean_tokens < 2000:
        rating, score = "Low", 100
    elif clean_tokens < 6000:
        rating, score = "Medium", 85
    elif clean_tokens < 15000:
        rating, score = "High", 65
    else:
        rating, score = "Very High", 40
    
    cost = (clean_tokens / 1000) * 0.03
    
    return TokenResult(
        score=score,
        rating=rating,
        clean_tokens=clean_tokens,
        estimated_cost_usd=round(cost, 4)
    )
```

### 3.2 为什么不用线性评分？

我们测试了线性评分，但发现：

**线性评分的问题**：
- 2000 tokens (优秀) vs 2100 tokens (良好) 只差 1.5 分
- 但用户感知不到差异，造成"不公平"

**阶梯评分的优势**：
- 清晰的等级边界
- 符合工程实践（类似 HTTP 状态码）
- 便于制定优化目标（"我要达到 Medium 级别"）

---

## 4. Permissions 算法

### 4.1 Robots.txt 解析

使用标准库 `urllib.robotparser`：

```python
from urllib.robotparser import RobotFileParser

def check_robots_txt(url: str, user_agent: str) -> bool:
    rp = RobotFileParser()
    rp.set_url(f"{base_url}/robots.txt")
    rp.read()
    return rp.can_fetch(user_agent, url)
```

### 4.2 检查的 Agent 列表

```python
AI_AGENTS = [
    'GPTBot',           # OpenAI
    'CCBot',            # Common Crawl
    'anthropic-ai',     # Anthropic
    'ClaudeBot',        # Anthropic
    'ChatGPT-User',     # OpenAI
    'Google-Extended',  # Google
    'PerplexityBot',    # Perplexity
]
```

### 4.3 llms.txt 检测

```python
def check_llms_txt(base_url: str) -> bool:
    for path in ['/llms.txt', '/.well-known/llms.txt']:
        try:
            response = requests.get(base_url + path, timeout=10)
            if response.status_code == 200 and len(response.text) > 10:
                return True
        except:
            continue
    return False
```

---

## 5. 权重设计原理

### 5.1 为什么是 30/30/20/20？

| 维度 | 权重 | 理由 |
|------|------|------|
| SNR | 30% | 直接影响 AI 阅读成本，最关键 |
| Semantic | 30% | 影响 AI 理解准确度，同样关键 |
| Token Economy | 20% | 与 SNR 相关，但侧重成本而非质量 |
| Permissions | 20% | 基础设施，但权重不宜过高 |

### 5.2 为什么不加入 Graceful Degradation？

我们尝试过检测"无 JS 时的内容可用性"，但发现：

**问题**：
- 现代框架（Next.js、Nuxt）的 SSR 会返回 HTML
- 但 HTML 里可能只是占位符 + hydration 数据
- 检测"内容质量" vs "有无内容" 很困难

**当前方案**：
用 SNR 间接反映。如果 SSR 返回的是有意义的 HTML，SNR 通常 > 20%。

---

## 6. 性能优化

### 6.1 并行处理

四个维度可以并行计算：

```python
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {
        'snr': executor.submit(analyze_snr, html),
        'semantic': executor.submit(analyze_semantic, soup),
        'token': executor.submit(analyze_token, snr_result),
        'permissions': executor.submit(analyze_permissions, url)
    }
    results = {k: f.result() for k, f in futures.items()}
```

### 6.2 缓存策略

建议缓存：
- robots.txt (TTL: 1小时)
- llms.txt (TTL: 24小时)
- 页面内容 (TTL: 根据网站更新频率)

---

## 7. 扩展维度（未来）

### 7.1 候选维度

- **Accessibility (a11y)**: 无障碍性通常也利于 AI
- **i18n**: 多语言支持质量
- **API Availability**: 是否有开放的 API 供 AI 使用
- **Freshness**: 内容更新频率

### 7.2 权重调整机制

未来可能根据网站类型动态调整权重：

```python
WEIGHTS = {
    'blog': {'snr': 0.4, 'semantic': 0.3, ...},
    'ecommerce': {'snr': 0.2, 'semantic': 0.4, ...},
    'docs': {'snr': 0.4, 'semantic': 0.2, ...}
}
```

---

## 8. 测试验证

### 8.1 单元测试

```python
def test_snr_high():
    html = "<html><body><h1>Title</h1><p>Content</p></body></html>"
    result = SNRAnalyzer().analyze(html)
    assert result.score >= 80
    assert result.snr_percent > 30
```

### 8.2 集成测试

测试真实网站，验证评分合理性：
- docs.python.org: 应该得 A 级
- medium.com: 应该得 C 级
- github.com: 应该得 B 级

---

## 9. 调试工具

### 9.1 详细输出模式

```bash
python -m openaix https://example.com --verbose
```

输出各维度的详细得分和计算过程。

### 9.2 基准测试

```bash
python benchmark.py --urls-file test_urls.txt --output report.md
```

生成对比报告，查看行业基准。

---

## 参考实现

完整的算法实现参见：
- `src/openaix/dimensions/snr.py`
- `src/openaix/dimensions/semantic.py`
- `src/openaix/dimensions/token.py`
- `src/openaix/dimensions/permissions.py`
