# OpenAIX Evaluation Report

**Target**: https://newyorker.com
**Score**: 41/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T11:15:46Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 1%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 8
- snr_percent: 1.3
- raw_tokens: 627636
- clean_tokens: 8175

### Semantic
- Score: 81
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 68
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8175
- estimated_cost_usd: 0.2453

### Permissions
- Score: 60
- allowed_agents: ['GPTBot', 'anthropic-ai', 'ChatGPT-User']
- blocked_agents: ['CCBot', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 67
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