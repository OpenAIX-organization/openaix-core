# OpenAIX Evaluation Report

**Target**: https://latimes.com
**Score**: 46/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-24T06:09:39Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 10%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 51
- snr_percent: 10.44
- raw_tokens: 516101
- clean_tokens: 53862

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 159
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 53862
- estimated_cost_usd: 1.6159

### Permissions
- Score: 80
- allowed_agents: ['CCBot', 'anthropic-ai', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'ClaudeBot']
- llms_txt_present: False
- response_time_ms: 56
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.