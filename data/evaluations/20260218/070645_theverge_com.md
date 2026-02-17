# OpenAIX Evaluation Report

**Target**: https://theverge.com
**Score**: 40/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T23:06:45Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 25
- snr_percent: 4.1
- raw_tokens: 352124
- clean_tokens: 14437

### Semantic
- Score: 74
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 65
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 14437
- estimated_cost_usd: 0.4331

### Permissions
- Score: 40
- allowed_agents: ['GPTBot']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 44
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