# OpenAIX Evaluation Report

**Target**: https://bloomberg.com
**Score**: 41/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-19T22:07:05Z
**Site Type**: documentation (confidence: 33%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 24
- snr_percent: 4.03
- raw_tokens: 4887
- clean_tokens: 197

### Semantic
- Score: 40
- semantic_tags_used: ['header', 'section']
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 197
- estimated_cost_usd: 0.0059

### Permissions
- Score: 0
- allowed_agents: []
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 153
- http_status: 403
- note: Access forbidden (HTTP 403)

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.bloomberg.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.