# OpenAIX Evaluation Report

**Target**: https://vuejs.org
**Score**: 54/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T19:15:09Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 25
- snr_percent: 4.22
- raw_tokens: 33415
- clean_tokens: 1410

### Semantic
- Score: 64
- semantic_tags_used: ['nav', 'header', 'main', 'section']
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1410
- estimated_cost_usd: 0.0423

### Permissions
- Score: 100
- allowed_agents: []
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 13
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://vuejs.org/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.