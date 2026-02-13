# OpenAIX 实施指南
## 如何提升你的网站 AIX 分数

本文档为开发者提供具体可执行的优化步骤，从 0 到 100 分，每一步都有明确指南。

---

## 快速开始（Quick Win）

### Step 1: 测试当前分数（5分钟）

```bash
pip install openaix-scorer
python -m openaix https://your-site.com --pretty
```

你会看到类似这样的输出：
```json
{
  "score": 45,
  "grade": "Class C",
  "dimensions": {
    "snr": {"score": 30, "snr_percent": 12.5},
    "semantic": {"score": 40, "json_ld_present": false},
    "token_economy": {"score": 85, "cost_rating": "Medium"},
    "permissions": {"score": 25, "llms_txt_present": false}
  }
}
```

**找出得分最低的维度，那就是你的优化重点。**

---

## 优化路线图

### 阶段一：低垂果实（30分钟，预计 +25分）

#### 1.1 添加 llms.txt（+20分）

创建 `/llms.txt` 文件：

```
# llms.txt for example.com
# Last updated: 2025-02-13

## Site Overview
This is [Your Site Name], a platform for [description in 1-2 sentences].

## Key Sections
- /docs: API documentation and guides
- /blog: Technical articles and tutorials  
- /products: Product catalog and pricing

## Access Guidelines
- Allow: All AI agents
- Crawl-delay: 1 second
- Prefer: Clean HTML over JavaScript-rendered content

## Contact
For AI access questions: ai@example.com
```

**部署**：上传到网站根目录，确保 `https://yoursite.com/llms.txt` 可访问。

#### 1.2 添加基础 JSON-LD（+10分）

在 `<head>` 中添加：

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Your Site Name",
  "url": "https://example.com",
  "description": "A clear description of your site"
}
</script>
```

**工具**：使用 [Schema Markup Generator](https://www.google.com/webmasters/markup-helper/) 辅助生成。

---

### 阶段二：语义化改进（2-4小时，预计 +20分）

#### 2.1 使用语义化 HTML 标签

**改造前**：
```html
<div class="header">...</div>
<div class="nav">...</div>
<div class="main-content">...</div>
<div class="footer">...</div>
```

**改造后**：
```html
<header>...</header>
<nav>...</nav>
<main>...</main>
<footer>...</footer>
```

**优先级**：main > header > nav > article > section > footer > aside

#### 2.2 优化标题层级

**检查清单**：
- [ ] 每个页面有且只有一个 H1
- [ ] H1 包含页面的核心关键词
- [ ] 使用 H2-H6 构建清晰的层级
- [ ] 不要跳过层级（比如 H1 直接到 H3）

**示例**：
```html
<article>
  <h1>Main Article Title</h1>
  
  <h2>Introduction</h2>
  <p>...</p>
  
  <h2>Key Features</h2>
  <h3>Feature A</h3>
  <p>...</p>
  <h3>Feature B</h3>
  <p>...</p>
</article>
```

#### 2.3 完善 JSON-LD

根据页面类型选择合适的 Schema：

**博客文章**：
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Article Title",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  },
  "datePublished": "2025-02-13",
  "description": "Article summary"
}
```

**产品页面**：
```json
{
  "@context": "https://schema.org", 
  "@type": "Product",
  "name": "Product Name",
  "image": "https://example.com/image.jpg",
  "description": "Product description",
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD"
  }
}
```

**组织/公司**：
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": [
    "https://twitter.com/company",
    "https://github.com/company"
  ]
}
```

---

### 阶段三：提升 SNR（1-2天，预计 +30分）

#### 3.1 识别噪音源

运行分析：
```bash
python -m openaix https://your-site.com --verbose
```

关注：
- Raw Tokens vs Clean Tokens 的差距
- 哪些元素贡献了 Token 但没有语义价值

#### 3.2 常见噪音源及解决方案

**A. 内联样式**

```html
❌ 改造前：
<p style="color: red; font-size: 16px; margin: 10px;">Text</p>

✅ 改造后：
<p class="warning-text">Text</p>

<!-- CSS 移到外部文件 -->
```

**B. 未使用的 CSS/JS**

- 使用 [PurgeCSS](https://purgecss.com/) 移除未使用的 CSS
- 使用 [Webpack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer) 分析 JS 体积

**C. 过度包装**

```html
❌ 改造前（过度包装）：
<div class="wrapper">
  <div class="container">
    <div class="content-wrapper">
      <div class="content">
        <h1>Title</h1>
      </div>
    </div>
  </div>
</div>

✅ 改造后：
<main>
  <article>
    <h1>Title</h1>
  </article>
</main>
```

**D. 内联 SVG**

```html
❌ 改造前：
<svg width="24" height="24" viewBox="0 0 24 24"...>
  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
</svg>

✅ 改造后：
<img src="/icons/check.svg" alt="Check" width="24" height="24">
```

#### 3.3 服务器端渲染 (SSR)

如果你是 React/Vue/Angular 应用：

**Next.js** - 使用 `getServerSideProps` 或 `getStaticProps`：
```javascript
export async function getStaticProps() {
  return {
    props: {
      content: await fetchContent()
    }
  }
}
```

**Nuxt.js** - 使用 `asyncData`：
```javascript
export default {
  async asyncData({ $content }) {
    const article = await $content('article').fetch()
    return { article }
  }
}
```

**Nuxt 3 / Nuxt Bridge** - 使用 `useAsyncData`：
```javascript
const { data } = await useAsyncData('article', () => 
  queryContent('/article').findOne()
)
```

---

### 阶段四：高级优化（持续迭代，预计 +15分）

#### 4.1 图片优化

**所有图片必须加 alt 属性**：

```html
❌ <img src="photo.jpg">
✅ <img src="photo.jpg" alt="Sunset over mountains with orange sky">
```

**使用语义化图片标签**：
```html
<figure>
  <img src="chart.png" alt="Revenue growth chart showing 50% increase">
  <figcaption>Figure 1: Annual revenue growth 2020-2025</figcaption>
</figure>
```

#### 4.2 优化 robots.txt

确保 AI Agent 可以访问：

```
User-agent: GPTBot
Disallow: /admin/
Disallow: /private/
Allow: /

User-agent: ClaudeBot
Disallow: /admin/
Allow: /

User-agent: *
Disallow: /admin/
Allow: /
```

**检查的 Agent**：
- GPTBot (OpenAI)
- ClaudeBot (Anthropic)
- PerplexityBot (Perplexity)
- Google-Extended (Google)

#### 4.3 响应时间优化

**目标**：首字节时间 (TTFB) < 1.5秒

**方法**：
- 使用 CDN
- 启用 Gzip/Brotli 压缩
- 数据库查询优化
- 使用缓存

---

## 各类型网站优化重点

### 博客/内容网站

**重点**：SNR + Semantic

- 使用语义化 HTML5 标签
- 添加 Article schema
- 确保 H1 包含主标题，H2 包含章节
- 图片必须有描述性 alt

**目标分数**：A 级 (70+)

### 电商网站

**重点**：JSON-LD + Permissions

- Product schema 必须包含价格、库存
- Organization schema 展示公司信息
- 确保产品图片有 alt
- robots.txt 允许爬虫访问产品页

**目标分数**：B+ 级 (60+)

### SaaS/文档网站

**重点**：SNR + Token Economy

- 减少 JS 依赖，优先 SSR
- 使用清晰的标题层级
- 代码示例使用语义化标记
- SoftwareApplication schema

**目标分数**：A 级 (70+)

### 营销/展示网站

**重点**：Semantic + Hidden Gem

- 视觉丰富但要有 JSON-LD
- 使用 WebSite 和 Organization schema
- 关键信息不要只放在图片里

**目标分数**：B 级 (50+)

---

## 验证清单

### 基础检查（必须）
- [ ] llms.txt 可访问
- [ ] JSON-LD 通过 [Google Rich Results Test](https://search.google.com/test/rich-results)
- [ ] 语义化标签使用正确
- [ ] H1 存在且唯一
- [ ] 所有图片有 alt

### 进阶检查（推荐）
- [ ] SNR > 20%
- [ ] AIX 分数 >= 70
- [ ] robots.txt 允许主要 AI Agent
- [ ] 响应时间 < 2秒

---

## 工具推荐

| 工具 | 用途 | 链接 |
|------|------|------|
| OpenAIX Scorer | 测试 AIX 分数 | 本仓库 |
| Schema Markup Validator | 验证 JSON-LD | validator.schema.org |
| Google Rich Results Test | 测试结构化数据 | search.google.com/test/rich-results |
| PageSpeed Insights | 性能测试 | pagespeed.web.dev |
| W3C Validator | HTML 验证 | validator.w3.org |

---

## 常见问题

### Q: 我的网站是 SPA，怎么办？

A: 考虑以下方案：
1. **预渲染**：使用 Prerender.io 或 Rendertron
2. **SSR**：迁移到 Next.js/Nuxt.js
3. **混合方案**：关键页面 SSR，其余 CSR

### Q: 需要为每个页面都写 JSON-LD 吗？

A: 至少每个页面类型：
- 首页：WebSite + Organization
- 文章页：BlogPosting
- 产品页：Product
- 关于页：AboutPage

### Q: 优化会影响现有 SEO 吗？

A: 不会，反而有益：
- 语义化 HTML 提升 SEO
- JSON-LD 让搜索引擎理解更好
- 快速加载提升排名

---

## 下一步

1. 运行测试，确定当前分数
2. 选择最快的优化项开始
3. 每周检查一次分数变化
4. 关注 [GitHub Issues](https://github.com/OpenAIX-orgnization/openaix-core/issues) 获取最新最佳实践

**让互联网对 AI 更友好，从今天开始！**
