# OpenAIX Evaluation Report

**Target**: https://adyen.com
**Score**: 43/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-28T16:04:52Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 2
- snr_percent: 0.41
- raw_tokens: 338304
- clean_tokens: 1385

### Semantic
- Score: 58
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 5
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1385
- estimated_cost_usd: 0.0415

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 53
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