# OpenAIX Evaluation Report

**Target**: https://zoom.com
**Score**: 60/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-23T05:07:52Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 14%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 58
- snr_percent: 13.89
- raw_tokens: 91429
- clean_tokens: 12697

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 105
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 12697
- estimated_cost_usd: 0.3809

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 166
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.zoom.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.