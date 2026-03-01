# OpenAIX Evaluation Report

**Target**: https://blazemeter.com
**Score**: 66/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T19:17:04Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 12%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 54
- snr_percent: 12.24
- raw_tokens: 29819
- clean_tokens: 3650

### Semantic
- Score: 76
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 14
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3650
- estimated_cost_usd: 0.1095

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 78
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.blazemeter.com', 'https://blazemeter.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.