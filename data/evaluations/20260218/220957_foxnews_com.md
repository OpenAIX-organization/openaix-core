# OpenAIX Evaluation Report

**Target**: https://foxnews.com
**Score**: 51/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T14:09:57Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 15%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 60
- snr_percent: 15.18
- raw_tokens: 230237
- clean_tokens: 34943

### Semantic
- Score: 90
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 206
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 34943
- estimated_cost_usd: 1.0483

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 14
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.