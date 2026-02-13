# OpenAIX
## The Web was built for eyes. We are indexing it for minds.

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-alpha-orange)]()

**OpenAIX** is an open standard that defines and quantifies **AIX (AI Experience)**—measuring how efficiently AI Agents (LLMs, RAG systems, crawlers) can access and understand web content.

---

## 🎉 Coming Soon

**We are building a web platform for testing your website's AIX score.**

Stay tuned! The testing platform will be launched soon.

In the meantime, you can explore our documentation:

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

→ [Read the Protocol Spec](spec/v1.0.md) - OpenAIX v1.0 Complete Definition

**Want to understand the scoring algorithm?**

→ [Read the Metrics](spec/metrics.md) - Four Dimension Calculation Formulas

**Want to optimize your website?**

→ [Read the Implementation Guide](spec/implementation.md) - 0 to 100 Points Optimization Roadmap

---

## 📊 The Four Dimensions

| Dimension | Weight | Measures | Key Metric |
|-----------|--------|----------|------------|
| **SNR** | 30% | Signal-to-Noise Ratio | Meaningful Content / Total Content |
| **Semantic** | 30% | Semantic Structure | Tags, JSON-LD, Metadata |
| **Token Economy** | 20% | Token Cost | AI Reading Cost |
| **Permissions** | 20% | Access Rights | robots.txt, llms.txt |

### Scoring Grades

| Grade | Score | Description | Example Sites |
|-------|-------|-------------|---------------|
| **S** | 85-100 | Silicon Native | Python Docs (84) |
| **A** | 70-84 | Agent Friendly | Apple.com (72) |
| **B** | 50-69 | Acceptable | GitHub (59) |
| **C** | < 50 | Needs Work | Unoptimized SPAs |

---

## 🏗️ Project Structure

```
openaix-core/
├── 📜 manifesto/          # Tao - Whitepapers and philosophy
│   ├── index.md          # Main manifesto
│   └── philosophy.md     # Dual-mode theory
│
├── 📋 spec/               # Shu - Technical specifications
│   ├── v1.0.md          # Protocol specification
│   ├── metrics.md       # Algorithm details
│   └── implementation.md # Optimization guide
│
├── ⚙️ src/                # Qi - Code implementation
│   └── openaix/
│       ├── scorer.py    # Scoring engine
│       ├── dimensions/  # Four dimension analyzers
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

### The Solution: Dual-Mode Internet

**Traditional**: Optimize only for human experience (UX)

**OpenAIX**: Optimize for both human experience + AI experience

| Optimization | For Humans | For AI |
|--------------|-----------|--------|
| JSON-LD | ✅ Rich media search | ✅ Structured understanding |
| Semantic HTML | ✅ Accessibility | ✅ Accurate parsing |
| Reduce noise | ✅ Fast loading | ✅ Low cost |

---

## 📈 Industry Benchmarks

**We tested 14 mainstream websites**:

- **Grade A (70+)**: Python Docs (84), Apple (72)
- **Grade B (50-69)**: Shopify (69), Notion (67), GitHub (59)
- **Grade C (<50)**: Medium (23) - blocked by Cloudflare

**Findings**:
- Traditional documentation sites perform best
- Modern SPAs need SSR optimization
- E-commerce sites need structured data

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
- [Protocol Spec v1.0](spec/v1.0.md) - Formal standard definition
- [Scoring Algorithms](spec/metrics.md) - Four dimensions in detail
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

## 📊 最新评测结果

| 网站 | 分数 | 等级 | 评测时间 |
|------|------|------|----------|
| openai.com | 15 | C | 2026-02-13 17:44 |

*最后更新: 2026-02-13 17:44:25*
<!-- EVALUATION_RESULTS_END -->
