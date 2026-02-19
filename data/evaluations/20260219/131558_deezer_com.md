# OpenAIX Evaluation Report

**Target**: https://deezer.com
**Score**: 57/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-19T05:15:58Z
**Site Type**: platform (confidence: 41%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 17
- snr_percent: 2.92
- raw_tokens: 80156
- clean_tokens: 2337

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 6
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2337
- estimated_cost_usd: 0.0701

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 459
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.deezer.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.