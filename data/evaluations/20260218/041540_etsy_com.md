# OpenAIX Evaluation Report

**Target**: https://etsy.com
**Score**: 32/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T20:15:40Z
**Site Type**: documentation (confidence: 0%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 19
- snr_percent: 3.12
- raw_tokens: 352
- clean_tokens: 11

### Semantic
- Score: 8
- semantic_tags_used: []
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 11
- estimated_cost_usd: 0.0003

### Permissions
- Score: 0
- allowed_agents: []
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 48
- http_status: 403
- note: Access forbidden (HTTP 403)

### Api Availability
- Score: 35
- features: ['api_subdomain', 'api_docs']
- endpoints_found: ['https://api.etsy.com', 'https://etsy.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.