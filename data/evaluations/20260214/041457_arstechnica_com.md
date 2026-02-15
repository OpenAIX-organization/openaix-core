# OpenAIX Evaluation Report

**Target**: https://arstechnica.com
**Score**: 58/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T20:14:57Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 8%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 42
- snr_percent: 7.97
- raw_tokens: 150638
- clean_tokens: 11999

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 61
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 11999
- estimated_cost_usd: 0.36

### Permissions
- Score: 50
- allowed_agents: ['GPTBot', 'ChatGPT-User']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 69
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.arstechnica.com', 'https://arstechnica.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.