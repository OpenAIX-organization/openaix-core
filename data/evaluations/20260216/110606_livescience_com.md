# OpenAIX Evaluation Report

**Target**: https://livescience.com
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-16T03:06:06Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 19
- snr_percent: 3.2
- raw_tokens: 388611
- clean_tokens: 12424

### Semantic
- Score: 89
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 78
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 12424
- estimated_cost_usd: 0.3727

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 53
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