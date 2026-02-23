# OpenAIX Evaluation Report

**Target**: https://nypost.com
**Score**: 45/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-23T16:16:30Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 6%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 34
- snr_percent: 6.04
- raw_tokens: 444436
- clean_tokens: 26827

### Semantic
- Score: 74
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 119
- heading_levels: 4
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 26827
- estimated_cost_usd: 0.8048

### Permissions
- Score: 45
- allowed_agents: ['GPTBot', 'ChatGPT-User']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 1548
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.nypost.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.