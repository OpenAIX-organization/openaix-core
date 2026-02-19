# OpenAIX Evaluation Report

**Target**: https://apps.apple.com
**Score**: 38/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-19T14:13:46Z
**Site Type**: platform (confidence: 41%)

---

## Metrics

- **snr**: 2%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 11
- snr_percent: 1.83
- raw_tokens: 459076
- clean_tokens: 8386

### Semantic
- Score: 54
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 108
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8386
- estimated_cost_usd: 0.2516

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 11
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
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.