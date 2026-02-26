# OpenAIX Evaluation Report

**Target**: https://thenationalnews.com
**Score**: 35/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T04:04:02Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 28
- snr_percent: 4.6
- raw_tokens: 333550
- clean_tokens: 15333

### Semantic
- Score: 47
- semantic_tags_used: ['header', 'section']
- json_ld_present: True
- hidden_gem: False
- images_total: 65
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 15333
- estimated_cost_usd: 0.46

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 92
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
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.