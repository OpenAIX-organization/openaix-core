# OpenAIX Evaluation Report

**Target**: https://weather.com
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-15T07:15:17Z
**Site Type**: platform (confidence: 41%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 14
- snr_percent: 2.37
- raw_tokens: 182447
- clean_tokens: 4331

### Semantic
- Score: 57
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 53
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4331
- estimated_cost_usd: 0.1299

### Permissions
- Score: 80
- allowed_agents: ['ChatGPT-User']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: True
- response_time_ms: 142
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.weather.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.