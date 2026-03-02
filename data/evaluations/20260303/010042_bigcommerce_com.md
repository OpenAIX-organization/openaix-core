# OpenAIX Evaluation Report

**Target**: https://bigcommerce.com
**Score**: 42/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T17:00:42Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 2%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 10
- snr_percent: 1.62
- raw_tokens: 386466
- clean_tokens: 6254

### Semantic
- Score: 68
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 48
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6254
- estimated_cost_usd: 0.1876

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 296
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