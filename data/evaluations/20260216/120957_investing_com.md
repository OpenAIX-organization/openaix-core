# OpenAIX Evaluation Report

**Target**: https://investing.com
**Score**: 45/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-16T04:09:57Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 23
- snr_percent: 3.78
- raw_tokens: 500362
- clean_tokens: 18894

### Semantic
- Score: 59
- semantic_tags_used: ['nav', 'header', 'section']
- json_ld_present: True
- hidden_gem: False
- images_total: 10
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 18894
- estimated_cost_usd: 0.5668

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 266
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.investing.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.