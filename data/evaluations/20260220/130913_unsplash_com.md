# OpenAIX Evaluation Report

**Target**: https://unsplash.com
**Score**: 40/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-20T05:09:13Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 11
- snr_percent: 1.76
- raw_tokens: 8998
- clean_tokens: 158

### Semantic
- Score: 30
- semantic_tags_used: ['main', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 1
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 158
- estimated_cost_usd: 0.0047

### Permissions
- Score: 0
- allowed_agents: []
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 127
- http_status: 401
- note: Access forbidden (HTTP 401)

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.unsplash.com', 'https://unsplash.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.