# OpenAIX Evaluation Report

**Target**: https://billboard.com
**Score**: 32/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-20T11:09:04Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 17
- snr_percent: 2.79
- raw_tokens: 636198
- clean_tokens: 17723

### Semantic
- Score: 67
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 96
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 17723
- estimated_cost_usd: 0.5317

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 12
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