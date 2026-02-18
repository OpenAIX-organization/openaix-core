# OpenAIX
## The Web was built for eyes. We are indexing it for minds.

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-alpha-orange)]()

**English** | [中文](README_CN.md)

**OpenAIX** is an open standard that defines and quantifies **AIX (AI Experience)**—measuring how efficiently AI Agents (LLMs, RAG systems, crawlers) can access and understand web content.

**Version 2.1** - Now with 5 dimensions, site type detection, and dynamic weights!

---

## 🎉 Coming Soon

**We are building a web platform for testing your website's AIX score.**

Stay tuned! The testing platform will be launched soon.

In the meantime, you can explore our documentation:

---

## 🆕 What's New in v2.1

### 5 Dimensions (was 4)
New **API Availability** dimension detects:
- OpenAPI/Swagger specifications
- GraphQL endpoints
- API subdomains (api.*)
- API documentation
- CLI tools

### Site Type Detection
Automatically classifies websites into 4 types:
- **Documentation** (Python Docs, MDN)
- **Product** (Apple, Shopify)
- **Platform** (GitHub, Vercel, Stripe) ← Now properly scored!
- **Content** (Medium, blogs)

### Dynamic Weights
Different weight profiles for different site types:

| Site Type | SNR | Semantic | API |
|-----------|-----|----------|-----|
| Documentation | 35% | 25% | 10% |
| Product | 25% | 35% | 15% |
| **Platform** | **15%** | 25% | **35%** |
| Content | 30% | 25% | 10% |

**Result**: GitHub scores improve from **59 (B)** to **~75 (A)** 🎉

### Multi-Page Sampling
Tests 3 pages per site (homepage + 2 representative pages) for fairer scoring.

---

## 📖 Documentation

### 👔 For Decision Makers / Product Managers / Investors

**Want to understand why AIX matters?**

→ [Read the Manifesto](manifesto/index.md) - "Rebuilding the Internet for the Agentic Web"

**Want to know why UX and AIX must coexist?**

→ [Read the Philosophy](manifesto/philosophy.md) - The Dual-Mode Internet Theory

**Key Insights**:
- 💰 AI companies spend **$10M+ annually** on web crawling
- 🔍 Your content may be buried under HTML noise
- 📈 High-AIX websites will gain traffic advantages in AI search

---

### 👨‍💻 For Developers / Engineers / CTOs

**Want to understand the technical specification?**

→ [Read Protocol Spec v1.1](spec/v1.1.md) - **Latest** - 5 dimensions, dynamic weights

→ [Read Protocol Spec v1.0](spec/v1.0.md) - Original 4-dimension specification

**Want to understand the scoring algorithm?**

→ [Read the Metrics](spec/metrics.md) - Five Dimension Calculation Formulas

**Want to optimize your website?**

→ [Read the Implementation Guide](spec/implementation.md) - 0 to 100 Points Optimization Roadmap

---

## 📊 The Five Dimensions

| Dimension | Weight* | Measures | Key Metric |
|-----------|---------|----------|------------|
| **SNR** | 15-35% | Signal-to-Noise Ratio | Meaningful Content / Total Content |
| **Semantic** | 25-35% | Semantic Structure | Tags, JSON-LD, Metadata |
| **Token Economy** | 15-25% | Token Cost | AI Reading Cost |
| **Permissions** | 10% | Access Rights | robots.txt, llms.txt |
| **API Availability** | 10-35% | Programmatic Access | OpenAPI, GraphQL, CLI |

\* Weight varies by site type (see Dynamic Weights above)

### Scoring Grades

| Grade | Score | Description | Example Sites (v2.1) |
|-------|-------|-------------|---------------------|
| **S** | 85-100 | Silicon Native | Python Docs (84) |
| **A** | 70-84 | Agent Friendly | **GitHub (~75)**, Apple (72), Stripe (~78) |
| **B** | 50-69 | Acceptable | Notion (~73), Shopify (69), Vercel (~72) |
| **C** | < 50 | Needs Work | Unoptimized SPAs, blocked sites |

**Note**: GitHub improved from 59 (B) to ~75 (A) in v2.1 due to API dimension and platform weighting!

---

## 🏗️ Project Structure

```
openaix-core/
├── 📜 manifesto/          # Tao - Whitepapers and philosophy
│   ├── index.md          # Main manifesto
│   └── philosophy.md     # Dual-mode theory
│
├── 📋 spec/               # Shu - Technical specifications
│   ├── v1.1.md          # Protocol v1.1 - 5 dimensions, dynamic weights ⭐
│   ├── v1.0.md          # Protocol v1.0 - Original 4 dimensions
│   ├── metrics.md       # Algorithm details
│   └── implementation.md # Optimization guide
│
├── ⚙️ src/                # Qi - Code implementation
│   └── openaix/
│       ├── scorer.py    # Scoring engine (v2.1)
│       ├── site_type.py # Site type detector
│       ├── weights.py   # Dynamic weight profiles
│       ├── dimensions/  # Five dimension analyzers
│       │   ├── snr.py
│       │   ├── semantic.py
│       │   ├── token.py
│       │   ├── permissions.py
│       │   └── api.py   # NEW: API availability
│       └── cli.py       # CLI tool
│
├── 🔧 benchmark.py       # Batch testing tool
├── 🧪 tests/            # Test suite
└── 📄 examples/         # Example code
```

**Design Philosophy**: Tao (manifesto) / Shu (spec) / Qi (code) - Three in One

---

## 🎯 Why OpenAIX?

### The Problem: AI Cannot Efficiently Read Modern Webpages

- Average webpage: 4MB, only 15% is semantic content
- GPT-4 cost to read one page: $0.03
- AI companies monthly crawling cost: **$1M+**
- **Platform sites unfairly penalized** for SPAs despite great APIs

### The Solution: Dual-Mode Internet + Fair Scoring

**Traditional**: Optimize only for human experience (UX)

**OpenAIX v2.1**: 
- Optimize for human experience + AI experience
- **Fair scoring for platform sites** (API-first companies)
- Site-type appropriate weighting

| Optimization | For Humans | For AI |
|--------------|-----------|--------|
| JSON-LD | ✅ Rich media search | ✅ Structured understanding |
| Semantic HTML | ✅ Accessibility | ✅ Accurate parsing |
| Reduce noise | ✅ Fast loading | ✅ Low cost |
| **API Documentation** | ✅ Dev tools | ✅ **Programmatic access** |

---

## 📈 Industry Benchmarks (v2.1)

**Improved scoring for platform sites**:

| Site | v1.0 Score | v2.1 Score | Improvement |
|------|-----------|-----------|-------------|
| **GitHub** | 59 (B) | **~75 (A)** | +16 points |
| **Vercel** | 59 (B) | **~72 (A)** | +13 points |
| **Stripe** | 54 (B) | **~78 (A)** | +24 points |
| **Notion** | 67 (B) | **~73 (A)** | +6 points |
| Python Docs | 84 (A) | 84 (A) | No change |
| Apple | 72 (A) | 72 (A) | No change |

**Why the improvement?** v2.1 properly values API availability and uses site-appropriate weights.

---

## 🤝 Contributing

We welcome all forms of contributions:

- 🐛 [Submit Bug](https://github.com/OpenAIX-organization/openaix-core/issues)
- 💡 [Propose Ideas](https://github.com/OpenAIX-organization/openaix-core/discussions)
- 📝 [Improve Documentation](spec/)
- 🔧 [Submit Code](CONTRIBUTING.md)

---

## 📚 Documentation Navigation

### Philosophy Layer
- [Main Manifesto](manifesto/index.md) - Why AIX matters
- [Dual-Mode Theory](manifesto/philosophy.md) - How UX and AIX coexist

### Technical Layer
- [Protocol Spec v1.1](spec/v1.1.md) - **Latest** - 5 dimensions, dynamic weights, multi-page
- [Protocol Spec v1.0](spec/v1.0.md) - Original 4-dimension spec
- [Scoring Algorithms](spec/metrics.md) - Five dimensions in detail
- [Implementation Guide](spec/implementation.md) - 0 to 100 points optimization

### Code Layer
- [API Docs](docs/API.md) - Python API reference
- [Architecture Docs](docs/ARCHITECTURE.md) - System architecture design
- [Examples](examples/) - Usage examples

---

## 📜 License

MIT © [OpenAIX.org](https://openaix.org)

---

## 🔗 Links

- **GitHub**: https://github.com/OpenAIX-organization/openaix-core
- **Issues**: [GitHub Issues](https://github.com/OpenAIX-organization/openaix-core/issues)
- **Discussions**: [GitHub Discussions](https://github.com/OpenAIX-organization/openaix-core/discussions)

---

**🎉 Testing platform coming soon! Stay tuned!**

**The Web was built for eyes. We are indexing it for minds.**

*Making the internet more AI-friendly, starting today.*


<!-- EVALUATION_RESULTS_START -->

## 📊 评测统计

- **总计评测网站**: 964 个
- **平均分数**: 48.3/100
- **最后更新**: 2026-02-19 01:18

### 等级分布

- **S**: 0 
- **A**: 41 █████████████████████████████████████████
- **B**: 282 ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
- **C**: 641 █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

### 最新评测结果

| 网站 | 分数 | 等级 | 评测时间 |
|------|------|------|----------|
| openai.com | 15 | C | 20260213_174419 |
| launchpad.net | 70 | B | 2026-02-19 01:18 |
| lefigaro.fr | 48 | C | 2026-02-19 01:18 |
| discord.gg | 73 | C | 2026-02-19 01:18 |
| fiverr.com | 65 | B | 2026-02-19 01:17 |
| networkadvertising.org | 55 | B | 2026-02-19 01:17 |
| federalregister.gov | 66 | B | 2026-02-19 01:16 |
| automattic.com | 64 | B | 2026-02-19 01:16 |
| naver.com | 32 | C | 2026-02-19 01:16 |
| eepurl.com | 75 | A | 2026-02-19 01:16 |
| play.google.com | 34 | C | 2026-02-19 01:16 |
| beian.miit.gov.cn | 30 | C | 2026-02-19 01:16 |
| npr.org | 49 | C | 2026-02-19 01:15 |
| youronlinechoices.com | 73 | A | 2026-02-19 01:15 |
| thenai.org | 55 | B | 2026-02-19 01:15 |
<!-- EVALUATION_RESULTS_END -->
