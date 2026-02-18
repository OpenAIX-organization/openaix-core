# OpenAIX Evaluation Report

**Target**: https://foursquare.com
**Score**: 63/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T09:07:30Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 13%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 55
- snr_percent: 12.54
- raw_tokens: 54723
- clean_tokens: 6861

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 90
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6861
- estimated_cost_usd: 0.2058

### Permissions
- Score: 80
- allowed_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'ChatGPT-User']
- llms_txt_present: False
- response_time_ms: 11
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.foursquare.com', 'https://foursquare.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.