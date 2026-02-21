# OpenAIX Evaluation Report

**Target**: https://nobelprize.org
**Score**: 59/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-21T12:15:50Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 10%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 50
- snr_percent: 10.21
- raw_tokens: 67442
- clean_tokens: 6888

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 41
- heading_levels: 6
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6888
- estimated_cost_usd: 0.2066

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 28
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.nobelprize.org']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.