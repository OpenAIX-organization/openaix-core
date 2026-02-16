# OpenAIX Evaluation Report

**Target**: https://typepad.com
**Score**: 25/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-16T06:15:16Z
**Site Type**: product (confidence: 100%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 0
- snr_percent: 0.02
- raw_tokens: 355743
- clean_tokens: 59

### Semantic
- Score: 15
- semantic_tags_used: ['header', 'section']
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 59
- estimated_cost_usd: 0.0018

### Permissions
- Score: 0
- allowed_agents: []
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 141
- http_status: 403
- note: Access forbidden (HTTP 403)

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.typepad.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.