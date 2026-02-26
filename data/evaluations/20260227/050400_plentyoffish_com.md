# OpenAIX Evaluation Report

**Target**: https://plentyoffish.com
**Score**: 56/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T21:04:00Z
**Site Type**: product (confidence: 100%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 28
- snr_percent: 4.73
- raw_tokens: 56573
- clean_tokens: 2675

### Semantic
- Score: 55
- semantic_tags_used: ['nav', 'header', 'main']
- json_ld_present: False
- hidden_gem: False
- images_total: 64
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2675
- estimated_cost_usd: 0.0802

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 76
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://plentyoffish.com/graphql', 'https://plentyoffish.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.