# OpenAIX Evaluation Report

**Target**: https://gitpod.io
**Score**: 38/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-27T11:06:27Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['api_subdomain', 'api_docs']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 6
- snr_percent: 1.0
- raw_tokens: 201
- clean_tokens: 2

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
- clean_tokens: 2
- estimated_cost_usd: 0.0001

### Permissions
- Score: 80
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: True
- response_time_ms: 31
- http_status: 200

### Api Availability
- Score: 35
- features: ['api_subdomain', 'api_docs']
- endpoints_found: ['https://api.gitpod.io', 'https://gitpod.io/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.