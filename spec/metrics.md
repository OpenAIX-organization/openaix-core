# OpenAIX Metrics Specification
## Detailed Algorithms for Four Scoring Dimensions

This document is for developers and architects, detailing the calculation methods and implementation details of OpenAIX scoring.

---

## 1. SNR (Signal-to-Noise Ratio) Algorithm

### 1.1 Algorithm Flow

```python
def calculate_snr(html: str) -> SNRResult:
    # Step 1: Calculate raw token count
    raw_tokens = count_tokens(html)
    
    # Step 2: Clean HTML
    soup = BeautifulSoup(html, 'lxml')
    for tag in ['script', 'style', 'noscript', 'iframe', 
                'canvas', 'svg', 'template', 'embed', 'object']:
        for element in soup.find_all(tag):
            element.decompose()
    
    # Step 3: Convert to Markdown
    clean_html = str(soup)
    markdown = markdownify(clean_html)
    
    # Step 4: Calculate clean token count
    clean_tokens = count_tokens(markdown)
    
    # Step 5: Calculate SNR
    snr = (clean_tokens / raw_tokens) * 100 if raw_tokens > 0 else 0
    
    # Step 6: Convert to score
    score = snr_to_score(snr)
    
    return SNRResult(
        score=score,
        snr_percent=snr,
        raw_tokens=raw_tokens,
        clean_tokens=clean_tokens
    )
```

### 1.2 Token Counter

Using `tiktoken` library with `cl100k_base` encoding:

```python
import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")
tokens = encoder.encode(text)
count = len(tokens)
```

### 1.3 Score Mapping Function

```python
def snr_to_score(snr: float) -> int:
    if snr >= 40:
        return 100
    elif snr >= 20:
        # Linear interpolation: 20% -> 70, 40% -> 100
        return int(70 + (snr - 20) * 1.5)
    elif snr >= 10:
        # Linear interpolation: 10% -> 50, 20% -> 70
        return int(50 + (snr - 10) * 2)
    elif snr >= 5:
        # Linear interpolation: 5% -> 30, 10% -> 50
        return int(30 + (snr - 5) * 4)
    else:
        # < 5%: Linear decrease
        return max(0, int(snr * 6))
```

### 1.4 Real-World Examples

| Website | Raw Tokens | Clean Tokens | SNR | Score |
|---------|-----------|--------------|-----|-------|
| docs.python.org | 15,000 | 13,800 | 92% | 100 |
| github.com | 45,000 | 5,400 | 12% | 54 |
| stripe.com/docs | 38,000 | 1,140 | 3% | 18 |

---

## 2. Semantic Structure Algorithm

### 2.1 Total Score Composition

```
Semantic Score = 
    semantic_tags(25) + 
    headings(25) + 
    json_ld(25) + 
    images(10) + 
    metadata(15)
```

### 2.2 Semantic Tag Detection

```python
SEMANTIC_TAGS = ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']

used_tags = [tag for tag in SEMANTIC_TAGS if soup.find(tag)]
score = (len(used_tags) / 7) * 25
```

### 2.3 JSON-LD Quality Assessment

```python
def analyze_json_ld(scripts: List[Tag]) -> int:
    if not scripts:
        return 0
    
    max_score = 0
    for script in scripts:
        try:
            data = json.loads(script.string)
            score = 0
            
            # Base points
            if '@context' in data:
                score += 5
            if '@type' in data:
                score += 5
            
            # Content quality
            important_fields = ['name', 'description', 'url', 
                              'author', 'datePublished', 'image']
            if any(f in data for f in important_fields):
                score += 5
            
            # Richness
            if len(script.string) > 500:
                score += 10
            
            max_score = max(max_score, score)
        except:
            continue
    
    return min(25, max_score)
```

### 2.4 Hidden Gem Detection

```python
def is_hidden_gem(soup: BeautifulSoup, snr: float, json_ld_score: int) -> bool:
    # Calculate text density
    text = soup.get_text(strip=True)
    html_str = str(soup)
    text_density = len(text) / len(html_str) if html_str else 1
    
    # Detection criteria
    return (
        text_density < 0.15 and           # Visually rich
        json_ld_score >= 15 and           # Good structured data
        bool(soup.find('h1')) and         # Basic content quality
        snr < 40                          # Low SNR (visual complexity)
    )
```

---

## 3. Token Economy Algorithm

### 3.1 Simple Tiered Scoring

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

### 3.2 Why Not Linear Scoring?

We tested linear scoring but found issues:

**Problem with Linear Scoring**:
- 2000 tokens (excellent) vs 2100 tokens (good) differs by only 1.5 points
- Users don't perceive this difference, causing "unfairness"

**Advantage of Tiered Scoring**:
- Clear grade boundaries
- Matches engineering practice (like HTTP status codes)
- Easy to set optimization goals ("I want to reach Medium level")

---

## 4. Permissions Algorithm

### 4.1 Robots.txt Parsing

Using standard library `urllib.robotparser`:

```python
from urllib.robotparser import RobotFileParser

def check_robots_txt(url: str, user_agent: str) -> bool:
    rp = RobotFileParser()
    rp.set_url(f"{base_url}/robots.txt")
    rp.read()
    return rp.can_fetch(user_agent, url)
```

### 4.2 Agents Checked

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

### 4.3 llms.txt Detection

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

## 5. Weight Design Principles

### 5.1 Why 30/30/20/20?

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| SNR | 30% | Directly affects AI reading cost, most critical |
| Semantic | 30% | Affects AI understanding accuracy, equally critical |
| Token Economy | 20% | Related to SNR, but focuses on cost not quality |
| Permissions | 20% | Infrastructure, but shouldn't dominate |

### 5.2 Why Not Include Graceful Degradation?

We tried detecting "content availability without JS" but found:

**Problem**:
- Modern frameworks (Next.js, Nuxt) SSR returns HTML
- But HTML may just be placeholders + hydration data
- Detecting "content quality" vs "has content" is difficult

**Current Solution**:
Use SNR to indirectly reflect. If SSR returns meaningful HTML, SNR is typically > 20%.

---

## 6. Performance Optimization

### 6.1 Parallel Processing

Four dimensions can be calculated in parallel:

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

### 6.2 Caching Strategy

Recommended caching:
- robots.txt (TTL: 1 hour)
- llms.txt (TTL: 24 hours)
- Page content (TTL: Based on website update frequency)

---

## 7. Extension Dimensions (Future)

### 7.1 Candidate Dimensions

- **Accessibility (a11y)**: Accessibility usually benefits AI too
- **i18n**: Multi-language support quality
- **API Availability**: Whether open API exists for AI use
- **Freshness**: Content update frequency

### 7.2 Dynamic Weight Adjustment

Future may dynamically adjust weights based on site type:

```python
WEIGHTS = {
    'blog': {'snr': 0.4, 'semantic': 0.3, ...},
    'ecommerce': {'snr': 0.2, 'semantic': 0.4, ...},
    'docs': {'snr': 0.4, 'semantic': 0.2, ...}
}
```

---

## 8. Testing and Validation

### 8.1 Unit Testing

```python
def test_snr_high():
    html = "<html><body><h1>Title</h1><p>Content</p></body></html>"
    result = SNRAnalyzer().analyze(html)
    assert result.score >= 80
    assert result.snr_percent > 30
```

### 8.2 Integration Testing

Test real websites to validate scoring reasonableness:
- docs.python.org: Should be Grade A
- medium.com: Should be Grade C
- github.com: Should be Grade B

---

## 9. Debugging Tools

### 9.1 Verbose Output Mode

```bash
python -m openaix https://example.com --verbose
```

Outputs detailed scores and calculation process for each dimension.

### 9.2 Benchmark Testing

```bash
python benchmark.py --urls-file test_urls.txt --output report.md
```

Generate comparison reports to view industry benchmarks.

---

## Reference Implementation

Complete algorithm implementations see:
- `src/openaix/dimensions/snr.py`
- `src/openaix/dimensions/semantic.py`
- `src/openaix/dimensions/token.py`
- `src/openaix/dimensions/permissions.py`
