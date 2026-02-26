# OpenAIX Evaluation Report

**Target**: https://redash.io
**Score**: 43/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T21:15:41Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 7
- snr_percent: 1.17
- raw_tokens: 58753
- clean_tokens: 686

### Semantic
- Score: 54
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 15
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 686
- estimated_cost_usd: 0.0206

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 36
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
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.