# OpenAIX Evaluation Report

**Target**: https://walmart.com
**Score**: 56/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T20:19:04Z
**Site Type**: product (confidence: 45%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 23
- snr_percent: 3.76
- raw_tokens: 110756
- clean_tokens: 4163

### Semantic
- Score: 56
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 14
- heading_levels: 1
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4163
- estimated_cost_usd: 0.1249

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 49
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://walmart.com/graphql', 'https://walmart.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.