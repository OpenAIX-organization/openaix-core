# OpenAIX Evaluation Report

**Target**: https://datadoghq.com/apm
**Score**: 56/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T02:15:24Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 14%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 57
- snr_percent: 13.62
- raw_tokens: 84794
- clean_tokens: 11553

### Semantic
- Score: 68
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 21
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 11553
- estimated_cost_usd: 0.3466

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 67
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.datadoghq.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.