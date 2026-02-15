# OpenAIX Evaluation Report

**Target**: https://upwork.com
**Score**: 33/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T23:09:47Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 4
- snr_percent: 0.6
- raw_tokens: 192400
- clean_tokens: 1157

### Semantic
- Score: 29
- semantic_tags_used: ['header', 'main', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1157
- estimated_cost_usd: 0.0347

### Permissions
- Score: 0
- allowed_agents: []
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 112
- http_status: 403
- note: Access forbidden (HTTP 403)

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.upwork.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.