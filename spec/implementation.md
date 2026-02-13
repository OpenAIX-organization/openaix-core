# OpenAIX Implementation Guide
## How to Improve Your Website AIX Score from 0 to 100

This document provides developers with concrete, actionable optimization steps, from 0 to 100 points, with clear guidelines for each step.

---

## Quick Start (Quick Wins)

### Step 1: Test Current Score (5 minutes)

```bash
pip install openaix-scorer
python -m openaix https://your-site.com --pretty
```

You'll see output like this:
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

**Identify the lowest-scoring dimension—that's your optimization priority.**

---

## Optimization Roadmap

### Phase 1: Low-Hanging Fruit (30 minutes, estimated +25 points)

#### 1.1 Add llms.txt (+20 points)

Create `/llms.txt` file:

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

**Deployment**: Upload to website root, ensure `https://yoursite.com/llms.txt` is accessible.

#### 1.2 Add Basic JSON-LD (+10 points)

Add to `<head>`:

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

**Tool**: Use [Schema Markup Generator](https://www.google.com/webmasters/markup-helper/) to assist generation.

---

### Phase 2: Semantic Improvements (2-4 hours, estimated +20 points)

#### 2.1 Use Semantic HTML Tags

**Before**:
```html
<div class="header">...</div>
<div class="nav">...</div>
<div class="main-content">...</div>
<div class="footer">...</div>
```

**After**:
```html
<header>...</header>
<nav>...</nav>
<main>...</main>
<footer>...</footer>
```

**Priority**: main > header > nav > article > section > footer > aside

#### 2.2 Optimize Heading Hierarchy

**Checklist**:
- [ ] Each page has exactly one H1
- [ ] H1 contains the page's core keywords
- [ ] Use H2-H6 to build clear hierarchy
- [ ] Don't skip levels (e.g., H1 directly to H3)

**Example**:
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

#### 2.3 Complete JSON-LD

Select appropriate Schema based on page type:

**Blog Post**:
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

**Product Page**:
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

**Organization/Company**:
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

### Phase 3: Improve SNR (1-2 days, estimated +30 points)

#### 3.1 Identify Noise Sources

Run analysis:
```bash
python -m openaix https://your-site.com --verbose
```

Focus on:
- Gap between Raw Tokens vs Clean Tokens
- Which elements contribute tokens without semantic value

#### 3.2 Common Noise Sources and Solutions

**A. Inline Styles**

```html
❌ Before:
<p style="color: red; font-size: 16px; margin: 10px;">Text</p>

✅ After:
<p class="warning-text">Text</p>

<!-- CSS moved to external file -->
```

**B. Unused CSS/JS**

- Use [PurgeCSS](https://purgecss.com/) to remove unused CSS
- Use [Webpack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer) to analyze JS size

**C. Excessive Wrappers**

```html
❌ Before (excessive wrapping):
<div class="wrapper">
  <div class="container">
    <div class="content-wrapper">
      <div class="content">
        <h1>Title</h1>
      </div>
    </div>
  </div>
</div>

✅ After:
<main>
  <article>
    <h1>Title</h1>
  </article>
</main>
```

**D. Inline SVG**

```html
❌ Before:
<svg width="24" height="24" viewBox="0 0 24 24"...>
  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
</svg>

✅ After:
<img src="/icons/check.svg" alt="Check" width="24" height="24">
```

#### 3.3 Server-Side Rendering (SSR)

If you're using React/Vue/Angular:

**Next.js** - Use `getServerSideProps` or `getStaticProps`:
```javascript
export async function getStaticProps() {
  return {
    props: {
      content: await fetchContent()
    }
  }
}
```

**Nuxt.js** - Use `asyncData`:
```javascript
export default {
  async asyncData({ $content }) {
    const article = await $content('article').fetch()
    return { article }
  }
}
```

**Nuxt 3 / Nuxt Bridge** - Use `useAsyncData`:
```javascript
const { data } = await useAsyncData('article', () => 
  queryContent('/article').findOne()
)
```

---

### Phase 4: Advanced Optimization (Continuous iteration, estimated +15 points)

#### 4.1 Image Optimization

**All images must have alt attributes**:

```html
❌ <img src="photo.jpg">
✅ <img src="photo.jpg" alt="Sunset over mountains with orange sky">
```

**Use semantic image tags**:
```html
<figure>
  <img src="chart.png" alt="Revenue growth chart showing 50% increase">
  <figcaption>Figure 1: Annual revenue growth 2020-2025</figcaption>
</figure>
```

#### 4.2 Optimize robots.txt

Ensure AI Agents can access:

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

**Agents to Check**:
- GPTBot (OpenAI)
- ClaudeBot (Anthropic)
- PerplexityBot (Perplexity)
- Google-Extended (Google)

#### 4.3 Response Time Optimization

**Goal**: Time to First Byte (TTFB) < 1.5 seconds

**Methods**:
- Use CDN
- Enable Gzip/Brotli compression
- Database query optimization
- Use caching

---

## Optimization Focus by Website Type

### Blog/Content Sites

**Focus**: SNR + Semantic

- Use semantic HTML5 tags
- Add Article schema
- Ensure H1 contains main title, H2 contains sections
- Images must have descriptive alt

**Target Score**: Grade A (70+)

### E-commerce Sites

**Focus**: JSON-LD + Permissions

- Product schema must include price, inventory
- Organization schema showing company info
- Ensure product images have alt
- robots.txt allows crawlers to access product pages

**Target Score**: Grade B+ (60+)

### SaaS/Documentation Sites

**Focus**: SNR + Token Economy

- Reduce JS dependency, prioritize SSR
- Use clear heading hierarchy
- Code examples use semantic markup
- SoftwareApplication schema

**Target Score**: Grade A (70+)

### Marketing/Showcase Sites

**Focus**: Semantic + Hidden Gem

- Visually rich but need JSON-LD
- Use WebSite and Organization schema
- Don't put key information only in images

**Target Score**: Grade B (50+)

---

## Validation Checklist

### Basic Checks (Required)
- [ ] llms.txt is accessible
- [ ] JSON-LD passes [Google Rich Results Test](https://search.google.com/test/rich-results)
- [ ] Semantic tags used correctly
- [ ] H1 exists and is unique
- [ ] All images have alt

### Advanced Checks (Recommended)
- [ ] SNR > 20%
- [ ] AIX Score >= 70
- [ ] robots.txt allows major AI Agents
- [ ] Response time < 2 seconds

---

## Recommended Tools

| Tool | Purpose | Link |
|------|---------|------|
| OpenAIX Scorer | Test AIX score | This repository |
| Schema Markup Validator | Validate JSON-LD | validator.schema.org |
| Google Rich Results Test | Test structured data | search.google.com/test/rich-results |
| PageSpeed Insights | Performance test | pagespeed.web.dev |
| W3C Validator | HTML validation | validator.w3.org |

---

## Frequently Asked Questions

### Q: My website is an SPA, what should I do?

A: Consider these options:
1. **Prerender**: Use Prerender.io or Rendertron
2. **SSR**: Migrate to Next.js/Nuxt.js
3. **Hybrid**: SSR for key pages, CSR for others

### Q: Do I need JSON-LD for every page?

A: At least for each page type:
- Homepage: WebSite + Organization
- Article pages: BlogPosting
- Product pages: Product
- About page: AboutPage

### Q: Will optimization affect existing SEO?

A: No, it will actually help:
- Semantic HTML improves SEO
- JSON-LD helps search engines understand better
- Fast loading improves rankings

---

## Next Steps

1. Run test to determine current score
2. Choose the fastest optimization item to start
3. Check score changes weekly
4. Follow [GitHub Issues](https://github.com/OpenAIX-organization/openaix-core/issues) for latest best practices

**Make the internet more AI-friendly, starting today!**
