# OpenAIX Evaluation Report

**Target**: https://theverge.com
**Score**: 33/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T23:08:46Z
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
- Score: 25
- snr_percent: 4.12
- raw_tokens: 369956
- clean_tokens: 15231

### Semantic
- Score: 64
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 77
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 15231
- estimated_cost_usd: 0.4569

### Permissions
- Score: 40
- allowed_agents: ['GPTBot']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 47
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