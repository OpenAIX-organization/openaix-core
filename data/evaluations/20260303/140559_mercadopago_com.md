# OpenAIX Evaluation Report

**Target**: https://mercadopago.com
**Score**: 46/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-03T06:05:59Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 28
- snr_percent: 4.61
- raw_tokens: 114762
- clean_tokens: 5294

### Semantic
- Score: 64
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 19
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 5294
- estimated_cost_usd: 0.1588

### Permissions
- Score: 100
- allowed_agents: []
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 462
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