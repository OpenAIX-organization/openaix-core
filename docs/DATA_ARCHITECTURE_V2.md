# OpenAIX 数据架构设计 v2.0

## 问题诊断

### 当前问题
1. **评分标准不一致**: 62分有时是B级，有时是C级
2. **历史数据丢失**: 只保留最新评测，无法追踪变化
3. **无法回查**: 不知道某次评测的具体时间、版本、方法

### 解决方案
采用**分层数据架构**：
- **Raw Layer**: 原始评测记录（保留所有历史）
- **Aggregated Layer**: 聚合数据（按网站去重，取最新/最优）
- **Standard Layer**: 评分标准版本管理

---

## 数据模型

### 1. 评测记录 (Evaluation Record)

```json
{
  "id": "eval_20260223_141533_twilio_com",
  "url": "https://twilio.com",
  "domain": "twilio.com",
  "evaluated_at": "2026-02-23T14:15:33Z",
  "evaluator_version": "2.1.0",
  
  "scores": {
    "snr": 27,
    "semantic": 89,
    "token": 65,
    "permissions": 100,
    "api": 45,
    "total": 62
  },
  
  "grade": "C",
  "grade_standard_version": "v3.0_percentile",
  
  "metadata": {
    "site_type": "platform",
    "page_count": 3,
    "raw_tokens": 227426,
    "clean_tokens": 10185,
    "snr_percent": 4.48
  },
  
  "features": {
    "json_ld": true,
    "llms_txt": true,
    "has_api": true,
    "robots_txt": true,
    "sitemap": true
  },
  
  "source": {
    "batch_id": "batch_20260223_001",
    "filename": "141533_twilio_com.md",
    "report_path": "data/evaluations/20260223/141533_twilio_com.md"
  }
}
```

### 2. 网站聚合数据 (Site Summary)

```json
{
  "domain": "twilio.com",
  "url": "https://twilio.com",
  "first_seen": "2026-02-15T10:30:00Z",
  "last_evaluated": "2026-02-23T14:15:33Z",
  
  "current": {
    "score": 62,
    "grade": "C",
    "site_type": "platform",
    "evaluated_at": "2026-02-23T14:15:33Z",
    "evaluator_version": "2.1.0"
  },
  
  "best": {
    "score": 65,
    "grade": "B",
    "evaluated_at": "2026-02-20T09:22:15Z"
  },
  
  "history": {
    "evaluation_count": 3,
    "score_trend": "stable",
    "average_score": 62.3
  },
  
  "evaluations": [
    "eval_20260223_141533_twilio_com",
    "eval_20260220_092215_twilio_com",
    "eval_20260215_103000_twilio_com"
  ]
}
```

### 3. 评分标准 (Grading Standard)

```json
{
  "version": "v3.0_percentile",
  "name": "Dynamic Percentile Ranking",
  "description": "基于百分位排名的动态等级划分",
  "effective_from": "2026-02-01T00:00:00Z",
  
  "method": "percentile",
  "thresholds": {
    "S": { "min_percentile": 98, "description": "Top 2%" },
    "A": { "min_percentile": 80, "description": "Top 20%" },
    "B": { "min_percentile": 50, "description": "Top 50%" },
    "C": { "min_percentile": 0, "description": "Bottom 50%" }
  },
  
  "calculation": {
    "formula": "percentile_rank",
    "recalculate_on": "each_batch",
    "current_thresholds": {
      "S": 75,
      "A": 63,
      "B": 52
    }
  }
}
```

---

## 目录结构

```
data/
├── evaluations/              # 原始评测记录（保留所有历史）
│   ├── 20260215/
│   │   ├── 103000_twilio_com.md
│   │   └── 110000_github_com.md
│   └── 20260223/
│       ├── 141533_twilio_com.md
│       └── 143000_github_com.md
│
├── sites/                    # 网站聚合数据（前端使用）
│   └── sites_index.json      # 所有网站的最新状态
│
├── standards/                # 评分标准版本
│   ├── v2.0_fixed.json       # 旧版固定阈值
│   ├── v3.0_percentile.json  # 当前动态百分位
│   └── current.json -> v3.0_percentile.json
│
└── exports/                  # 前端导出数据
    ├── rankings_current.json    # 当前分数排行
    ├── rankings_best.json       # 历史最高排行
    └── rankings_history.json    # 变化趋势数据
```

---

## 数据流程

### 1. 评测流程
```
评测脚本
    ↓
生成评测报告 → data/evaluations/{date}/{timestamp}_{domain}.md
    ↓
更新网站聚合数据 → data/sites/sites_index.json
    ↓
重新计算百分位阈值
    ↓
更新等级（如果需要）
    ↓
导出前端数据 → data/exports/
```

### 2. 等级计算逻辑

```python
def calculate_grade(score, all_scores, standard_version="v3.0_percentile"):
    """
    统一的等级计算函数
    """
    if standard_version == "v3.0_percentile":
        # 动态百分位
        percentile = calculate_percentile(score, all_scores)
        if percentile >= 98: return "S"
        if percentile >= 80: return "A"
        if percentile >= 50: return "B"
        return "C"
    else:
        # 固定阈值
        if score >= 80: return "S"
        if score >= 65: return "A"
        if score >= 50: return "B"
        return "C"
```

### 3. 数据一致性修复

```python
def migrate_and_standardize():
    """
    修复历史数据，统一标准
    """
    for site in all_sites:
        # 1. 使用当前标准重新计算等级
        site.current.grade = calculate_grade(
            site.current.score, 
            all_current_scores,
            "v3.0_percentile"
        )
        
        # 2. 保留历史评测记录，但标记使用的标准版本
        for eval_record in site.evaluations:
            eval_record.grade_standard_version = detect_version(eval_record)
```

---

## 前端数据格式

### rankings_current.json
```json
{
  "meta": {
    "generated_at": "2026-02-23T15:00:00Z",
    "standard_version": "v3.0_percentile",
    "total_sites": 930,
    "data_source": "current"
  },
  "sites": [
    {
      "rank": 1,
      "domain": "zoho.com",
      "url": "https://zoho.com",
      "score": 84,
      "grade": "A",
      "site_type": "product",
      "features": {
        "llms_txt": false,
        "json_ld": true,
        "has_api": true
      }
    }
  ]
}
```

---

## 实现建议

### Phase 1: 数据迁移（立即）
1. 保留所有原始评测文件
2. 使用当前标准重新计算所有等级
3. 生成统一的 `sites_index.json`

### Phase 2: 标准固化（本周）
1. 选择一种标准（建议固定阈值，更易理解）
2. 锁定等级计算方法
3. 更新所有历史数据

### Phase 3: 历史追踪（下周）
1. 实现多次评测记录
2. 添加趋势分析
3. 显示"最佳分数" vs "当前分数"

---

## 推荐方案

### 方案A: 固定阈值（推荐）
- **S**: 80-100
- **A**: 65-79
- **B**: 50-64
- **C**: 0-49

**优点**: 简单直观，容易理解，稳定可预期
**缺点**: 可能随时间分布不均

### 方案B: 动态百分位（现状）
- **S**: Top 2%
- **A**: Top 20%
- **B**: Top 50%
- **C**: Bottom 50%

**优点**: 始终保持分布合理
**缺点**: 复杂，等级阈值会变，用户困惑

---

## 下一步行动

1. **选择标准**: 你想用固定阈值还是动态百分位？
2. **重新计算**: 我来写一个脚本，统一所有数据的等级
3. **迁移数据**: 建立新的数据架构
4. **更新前端**: 加载新的数据结构

建议：用**固定阈值**，简单明了。你觉得呢？