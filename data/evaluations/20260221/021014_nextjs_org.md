# OpenAIX Evaluation Report

**Target**: https://nextjs.org
**Score**: 59/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-20T18:10:14Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 23
- snr_percent: 3.85
- raw_tokens: 122574
- clean_tokens: 4713

### Semantic
- Score: 68
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 33
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4713
- estimated_cost_usd: 0.1414

### Permissions
- Score: 100
- allowed_agents: []
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 44
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.nextjs.org', 'https://nextjs.org/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.