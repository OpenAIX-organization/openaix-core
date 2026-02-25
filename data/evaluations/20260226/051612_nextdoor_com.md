# OpenAIX Evaluation Report

**Target**: https://nextdoor.com
**Score**: 32/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T21:16:12Z
**Site Type**: platform (confidence: 62%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 1
- snr_percent: 0.08
- raw_tokens: 9523
- clean_tokens: 8

### Semantic
- Score: 15
- semantic_tags_used: []
- json_ld_present: True
- hidden_gem: False
- images_total: 0
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 8
- estimated_cost_usd: 0.0002

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 89
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.nextdoor.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.