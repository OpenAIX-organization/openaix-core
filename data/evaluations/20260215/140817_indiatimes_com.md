# OpenAIX Evaluation Report

**Target**: https://indiatimes.com
**Score**: 55/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-15T06:08:17Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 13%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 56
- snr_percent: 13.03
- raw_tokens: 33834
- clean_tokens: 4409

### Semantic
- Score: 54
- semantic_tags_used: ['article', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 41
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4409
- estimated_cost_usd: 0.1323

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 12
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.indiatimes.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.