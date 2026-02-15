# OpenAIX Evaluation Report

**Target**: https://nasa.gov
**Score**: 59/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T21:18:26Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 10%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 49
- snr_percent: 9.85
- raw_tokens: 105483
- clean_tokens: 10395

### Semantic
- Score: 63
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 71
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 10395
- estimated_cost_usd: 0.3118

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 7
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.nasa.gov', 'https://nasa.gov/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.