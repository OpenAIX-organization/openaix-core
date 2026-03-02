# OpenAIX Evaluation Report

**Target**: https://volvocars.com
**Score**: 45/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T08:16:05Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 14
- snr_percent: 2.35
- raw_tokens: 158979
- clean_tokens: 3743

### Semantic
- Score: 67
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 85
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3743
- estimated_cost_usd: 0.1123

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 220
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.