# OpenAIX
## The Web was built for eyes. We are indexing it for minds.

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-alpha-orange)]()

[English](README.md) | **中文**

**OpenAIX** 是一个开放标准，用于定义和量化 **AIX（AI Experience，AI 体验）**——衡量 AI Agent（LLM、RAG 系统、爬虫）访问和理解网页内容的效率。

**版本 2.1** - 现已支持 5 大维度、网站类型检测和动态权重！

---

## 🎉 即将推出

**我们正在构建一个用于测试网站 AIX 分数的 Web 平台。**

敬请期待！测试平台即将上线。

在此期间，你可以浏览我们的文档：

---

## 🆕 v2.1 新特性

### 5 大维度（原来是 4 个）
新增 **API 可用性** 维度，检测：
- OpenAPI/Swagger 规范
- GraphQL 端点
- API 子域名（api.*）
- API 文档
- CLI 工具

### 网站类型检测
自动将网站分类为 4 种类型：
- **文档站**（Python Docs、MDN）
- **产品站**（Apple、Shopify）
- **平台站**（GitHub、Vercel、Stripe）← 现在能正确评分了！
- **内容站**（Medium、博客）

### 动态权重
根据网站类型使用不同的权重配置：

| 网站类型 | SNR | 语义 | API |
|---------|-----|------|-----|
| 文档站 | 35% | 25% | 10% |
| 产品站 | 25% | 35% | 15% |
| **平台站** | **15%** | 25% | **35%** |
| 内容站 | 30% | 25% | 10% |

**结果**：GitHub 分数从 **59 (B)** 提升到 **~75 (A)** 🎉

### 多页面采样
每个站点测试 3 个页面（首页 + 2 个代表性页面），评分更公平。

---

## 📖 文档

### 👔 决策者 / 产品经理 / 投资人

**想了解为什么 AIX 很重要？**

→ [阅读白皮书](manifesto/index.md) - "为智能体网络重构互联网"

**想知道为什么 UX 和 AIX 必须共存？**

→ [阅读双模理论](manifesto/philosophy.md) - 双模互联网理论

**关键洞察**：
- 💰 AI 公司每年在网页爬取上花费 **1000 万美元以上**
- 🔍 你的内容可能被埋在 HTML 噪音之下
- 📈 高 AIX 网站将在 AI 搜索中获得流量优势

---

### 👨‍💻 开发者 / 工程师 / CTO

**想了解技术规范？**

→ [阅读协议规范 v1.1](spec/v1.1.md) - **最新** - 5 大维度、动态权重

→ [阅读协议规范 v1.0](spec/v1.0.md) - 原始 4 维度规范

**想了解评分算法？**

→ [阅读算法详解](spec/metrics.md) - 五大维度计算公式

**想优化你的网站？**

→ [阅读实施指南](spec/implementation.md) - 0 到 100 分优化路线图

---

## 📊 五大维度

| 维度 | 权重* | 衡量内容 | 关键指标 |
|-----|------|---------|---------|
| **SNR** | 15-35% | 信噪比 | 有效内容 / 总内容 |
| **语义** | 25-35% | 语义结构 | 标签、JSON-LD、元数据 |
| **Token 经济** | 15-25% | Token 成本 | AI 阅读成本 |
| **权限** | 10% | 访问权限 | robots.txt、llms.txt |
| **API 可用性** | 10-35% | 程序化访问 | OpenAPI、GraphQL、CLI |

\* 权重根据网站类型变化（见上文动态权重）

### 评分等级

| 等级 | 分数 | 描述 | 示例网站 (v2.1) |
|-----|------|-----|----------------|
| **S** | 85-100 | 原生硅基 | Python Docs (84) |
| **A** | 70-84 | 智能体友好 | **GitHub (~75)**、Apple (72)、Stripe (~78) |
| **B** | 50-69 | 可接受 | Notion (~73)、Shopify (69)、Vercel (~72) |
| **C** | < 50 | 需改进 | 未优化的 SPA、被屏蔽的网站 |

**注意**：GitHub 在 v2.1 中从 59 (B) 提升到 ~75 (A)，这要归功于 API 维度和平台站权重！

---

## 🏗️ 项目结构

```
openaix-core/
├── 📜 manifesto/          # 道 - 白皮书和理念
│   ├── index.md          # 主宣言
│   └── philosophy.md     # 双模理论
│
├── 📋 spec/               # 术 - 技术规范
│   ├── v1.1.md          # 协议 v1.1 - 5 维度、动态权重 ⭐
│   ├── v1.0.md          # 协议 v1.0 - 原始 4 维度
│   ├── metrics.md       # 算法详情
│   └── implementation.md # 优化指南
│
├── ⚙️ src/                # 器 - 代码实现
│   └── openaix/
│       ├── scorer.py    # 评分引擎 (v2.1)
│       ├── site_type.py # 网站类型检测器
│       ├── weights.py   # 动态权重配置
│       ├── storage.py   # 数据存储工具
│       ├── dimensions/  # 五大维度分析器
│       │   ├── snr.py
│       │   ├── semantic.py
│       │   ├── token.py
│       │   ├── permissions.py
│       │   └── api.py   # 新增：API 可用性
│       └── cli.py       # CLI 工具
│
├── 📁 data/               # 评测数据（自动创建）
│   └── evaluations/
│       └── 20260213/
│           ├── 143052_github_com.json
│           └── 143052_github_com.md
│
├── 🔧 benchmark.py       # 批量测试工具
├── 🧪 tests/            # 测试套件
└── 📄 examples/         # 示例代码
```

**设计理念**：道（manifesto）/ 术（spec）/ 器（code）- 三位一体

---

## 🎯 为什么需要 OpenAIX？

### 问题：AI 无法高效读取现代网页

- 平均网页：4MB，只有 15% 是语义内容
- GPT-4 读取一页成本：$0.03
- AI 公司每月爬取成本：**100 万美元以上**
- **平台站因 SPA 被不公平地惩罚**，尽管它们有很好的 API

### 解决方案：双模互联网 + 公平评分

**传统**：只优化人类体验（UX）

**OpenAIX v2.1**：
- 同时优化人类体验 + AI 体验
- **为平台站提供公平评分**（API 优先的公司）
- 根据网站类型使用适当的权重

| 优化项 | 对人类 | 对 AI |
|--------|--------|-------|
| JSON-LD | ✅ 富媒体搜索 | ✅ 结构化理解 |
| 语义 HTML | ✅ 无障碍 | ✅ 准确解析 |
| 减少噪音 | ✅ 快速加载 | ✅ 低成本 |
| **API 文档** | ✅ 开发者工具 | ✅ **程序化访问** |

---

## 📈 行业基准 (v2.1)

**平台站评分显著改善**：

| 网站 | v1.0 分数 | v2.1 分数 | 提升 |
|-----|----------|----------|------|
| **GitHub** | 59 (B) | **~75 (A)** | +16 分 |
| **Vercel** | 59 (B) | **~72 (A)** | +13 分 |
| **Stripe** | 54 (B) | **~78 (A)** | +24 分 |
| **Notion** | 67 (B) | **~73 (A)** | +6 分 |
| Python Docs | 84 (A) | 84 (A) | 无变化 |
| Apple | 72 (A) | 72 (A) | 无变化 |

**为什么有提升？** v2.1 正确评估了 API 可用性并使用网站类型适当的权重。

---

## 💾 数据存储

评测数据自动保存到标准化位置：

```
data/evaluations/YYYYMMDD/
  - {timestamp}_{site_name}.json    # 机器可读数据
  - {timestamp}_{site_name}.md      # 人类可读报告
```

**示例**：
```bash
python -m openaix https://github.com
# 保存到：data/evaluations/20260213/143052_github_com.json
```

---

## 🤝 贡献

我们欢迎各种形式的贡献：

- 🐛 [提交 Bug](https://github.com/OpenAIX-organization/openaix-core/issues)
- 💡 [提出想法](https://github.com/OpenAIX-organization/openaix-core/discussions)
- 📝 [改进文档](spec/)
- 🔧 [提交代码](CONTRIBUTING.md)

---

## 📚 文档导航

### 理念层
- [主宣言](manifesto/index.md) - 为什么 AIX 很重要
- [双模理论](manifesto/philosophy.md) - UX 与 AIX 如何共存

### 技术层
- [协议规范 v1.1](spec/v1.1.md) - **最新** - 5 维度、动态权重、多页面
- [协议规范 v1.0](spec/v1.0.md) - 原始 4 维度规范
- [评分算法](spec/metrics.md) - 五大维度详解
- [实施指南](spec/implementation.md) - 0 到 100 分优化

### 代码层
- [API 文档](docs/API.md) - Python API 参考
- [架构文档](docs/ARCHITECTURE.md) - 系统架构设计
- [示例](examples/) - 使用示例

---

## 📜 许可证

MIT © [OpenAIX.org](https://openaix.org)

---

## 🔗 链接

- **GitHub**: https://github.com/OpenAIX-organization/openaix-core
- **Issues**: [GitHub Issues](https://github.com/OpenAIX-organization/openaix-core/issues)
- **Discussions**: [GitHub Discussions](https://github.com/OpenAIX-organization/openaix-core/discussions)

---

**🎉 测试平台即将上线！敬请期待！**

**The Web was built for eyes. We are indexing it for minds.**

*让互联网对 AI 更友好，从今天开始。*
