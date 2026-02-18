# OpenAIX Evaluation Report

**Target**: https://elpais.com
**Score**: 58/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T05:11:03Z
**Site Type**: platform (confidence: 50%)

---

## Metrics

- **snr**: 20%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 70
- snr_percent: 19.81
- raw_tokens: 140327
- clean_tokens: 27793

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 114
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 27793
- estimated_cost_usd: 0.8338

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 186
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.elpais.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.