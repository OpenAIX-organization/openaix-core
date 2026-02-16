# OpenAIX Evaluation Report

**Target**: https://huffingtonpost.com
**Score**: 38/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-16T02:07:40Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 27
- snr_percent: 4.49
- raw_tokens: 429876
- clean_tokens: 19292

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 109
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 19292
- estimated_cost_usd: 0.5788

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 13
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.