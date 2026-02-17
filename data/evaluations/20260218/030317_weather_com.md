# OpenAIX Evaluation Report

**Target**: https://weather.com
**Score**: 47/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T19:03:17Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 1%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 5
- snr_percent: 0.79
- raw_tokens: 829140
- clean_tokens: 6588

### Semantic
- Score: 73
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 57
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6588
- estimated_cost_usd: 0.1976

### Permissions
- Score: 80
- allowed_agents: ['ChatGPT-User']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: True
- response_time_ms: 152
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