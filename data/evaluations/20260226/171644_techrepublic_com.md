# OpenAIX Evaluation Report

**Target**: https://techrepublic.com
**Score**: 57/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T09:16:44Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 6%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 35
- snr_percent: 6.26
- raw_tokens: 162232
- clean_tokens: 10148

### Semantic
- Score: 86
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 67
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 10148
- estimated_cost_usd: 0.3044

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 36
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.techrepublic.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.