# OpenAIX
## The Web was built for eyes. We are indexing it for minds.

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](pyproject.toml)
[![Status](https://img.shields.io/badge/status-alpha-orange)]()

**OpenAIX** 是一个开源标准，定义和量化网站的 **AIX（AI Experience）**——衡量 AI Agent（LLM、RAG系统、爬虫）访问和理解网页的效率。

---

## 🚀 快速开始

```bash
# 安装
pip install openaix-scorer

# 测试你的网站
python -m openaix https://your-site.com

# 生成详细报告
python -m openaix https://your-site.com --format md --output report.md
```

---

## 📖 你是哪类读者？

### 👔 我是决策者 / 产品经理 / 投资人

**想了解为什么 AIX 很重要？**

→ [阅读白皮书](manifesto/index.md) - 《为智能体网络重构互联网》

**想知道为什么 UX 和 AIX 必须共存？**

→ [阅读哲学](manifesto/philosophy.md) - 双模互联网理论

**关键洞察**：
- 💰 AI 公司每年花费 **$1000万+** 在网页爬取上
- 🔍 你的内容可能被埋在 HTML 噪音之下
- 📈 高 AIX 网站将获得 AI 搜索的流量红利

---

### 👨‍💻 我是开发者 / 工程师 / CTO

**想了解技术规范和实现？**

→ [阅读协议规范](spec/v1.0.md) - OpenAIX v1.0 完整定义

**想了解评分算法？**

→ [阅读算法详解](spec/metrics.md) - 四大维度计算公式

**想优化你的网站？**

→ [阅读实施指南](spec/implementation.md) - 从 0 到 100 分的优化路线图

**快速优化清单**：
- [ ] 添加 `llms.txt` (+20分)
- [ ] 添加 JSON-LD 结构化数据 (+15分)
- [ ] 使用语义化 HTML 标签 (+10分)
- [ ] 优化 HTML 噪音 (+30分)

---

## 📊 评分概览

### 四大维度

| 维度 | 权重 | 衡量什么 | 关键指标 |
|------|------|----------|----------|
| **SNR** | 30% | 信噪比 | 有效内容 / 总内容 |
| **Semantic** | 30% | 语义结构 | 标签、JSON-LD、元数据 |
| **Token Economy** | 20% | Token 成本 | AI 阅读成本 |
| **Permissions** | 20% | 访问权限 | robots.txt, llms.txt |

### 评分等级

| 等级 | 分数 | 描述 | 典型网站 |
|------|------|------|----------|
| **S** | 85-100 | Silicon Native | Python Docs (84) |
| **A** | 70-84 | Agent Friendly | Apple.com (72) |
| **B** | 50-69 | Acceptable | GitHub (59) |
| **C** | < 50 | Needs Work | SPA 未优化站点 |

**查看详细基准数据**：[benchmark_report_v2.md](output/benchmark_report_v2.md)

---

## 🏗️ 项目结构

```
openaix-core/
├── 📜 manifesto/          # 道 - 白皮书和理念
│   ├── index.md          # 主宣言
│   └── philosophy.md     # 双模理论
│
├── 📋 spec/               # 术 - 技术规范
│   ├── v1.0.md          # 协议规范
│   ├── metrics.md       # 算法详解
│   └── implementation.md # 实施指南
│
├── ⚙️ src/                # 器 - 代码实现
│   └── openaix/
│       ├── scorer.py    # 评分引擎
│       ├── dimensions/  # 四维度分析器
│       └── cli.py       # 命令行工具
│
├── 🔧 benchmark.py       # 批量测试工具
├── 🧪 tests/             # 测试套件
└── 📄 examples/          # 示例代码
```

**设计理念**：道（Manifesto）/ 术（Spec）/ 器（Code）三位一体

---

## 💻 开发者指南

### 安装

```bash
# 克隆仓库
git clone https://github.com/OpenAIX-orgnization/openaix-core.git
cd openaix-core

# 安装（开发模式）
pip install -e ".[dev]"
```

### 使用

```python
from openaix import OpenAIXScorer

scorer = OpenAIXScorer()
result = scorer.score("https://example.com")

print(f"AIX Score: {result['score']}/100")
print(f"Grade: {result['grade']}")
print(f"SNR: {result['dimensions']['snr']['snr_percent']:.1f}%")
```

### 批量测试

```bash
# 测试多个 URL
python benchmark.py https://site1.com https://site2.com

# 从文件读取
python benchmark.py --urls-file urls.txt --output report.md
```

---

## 🎯 为什么需要 OpenAIX？

### 问题：AI 无法高效读取现代网页

- 平均网页 4MB，只有 15% 是语义内容
- GPT-4 读取一个页面的成本：$0.03
- AI 公司每月爬取成本：**$100万+**

### 解决方案：双模互联网

**传统**：只优化人类体验（UX）

**OpenAIX**：同时优化人类体验 + AI 体验

| 优化项 | 对人类 | 对 AI |
|--------|--------|-------|
| JSON-LD | ✅ 富媒体搜索 | ✅ 结构化理解 |
| 语义 HTML | ✅ 无障碍 | ✅ 准确解析 |
| 减少噪音 | ✅ 加载快 | ✅ 低成本 |

---

## 📈 行业基准

**我们测试了 14 个主流网站**：

- **A 级 (70+)**：Python Docs (84), Apple (72)
- **B 级 (50-69)**：Shopify (69), Notion (67), GitHub (59)
- **C 级 (<50)**：Medium (23) - 被 Cloudflare 阻挡

**发现**：
- 传统文档站点表现最好
- 现代 SPA 需要 SSR 优化
- 电商站点结构化数据至关重要

---

## 🤝 贡献

我们欢迎所有形式的贡献：

- 🐛 [提交 Bug](https://github.com/OpenAIX-orgnization/openaix-core/issues)
- 💡 [提出新想法](https://github.com/OpenAIX-orgnization/openaix-core/discussions)
- 📝 [改进文档](spec/)
- 🔧 [提交代码](CONTRIBUTING.md)

---

## 📚 文档导航

### 理念层
- [主宣言](manifesto/index.md) - 为什么 AIX 很重要
- [双模理论](manifesto/philosophy.md) - UX 与 AIX 如何共存

### 技术层
- [协议规范 v1.0](spec/v1.0.md) - 正式标准定义
- [评分算法](spec/metrics.md) - 四大维度详解
- [实施指南](spec/implementation.md) - 从 0 到 100 分优化

### 代码层
- [API 文档](docs/API.md) - Python API 参考
- [架构文档](docs/ARCHITECTURE.md) - 系统架构设计
- [示例代码](examples/) - 使用示例

---

## 📜 许可证

MIT © [OpenAIX.org](https://openaix.org)

---

## 🔗 相关链接

- **GitHub**: https://github.com/OpenAIX-orgnization/openaix-core
- **问题反馈**: [GitHub Issues](https://github.com/OpenAIX-orgnization/openaix-core/issues)
- **讨论区**: [GitHub Discussions](https://github.com/OpenAIX-orgnization/openaix-core/discussions)

---

**The Web was built for eyes. We are indexing it for minds.**

*让互联网对 AI 更友好，从今天开始。*
