# OpenAIX Evaluation Report

**Target**: https://anchor.fm
**Score**: 66/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T01:16:10Z
**Site Type**: product (confidence: 50%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['openapi_spec', 'graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 4

---

## Dimensions


### Snr
- Score: 23
- snr_percent: 3.81
- raw_tokens: 30910
- clean_tokens: 1178

### Semantic
- Score: 58
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 8
- heading_levels: 1
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1178
- estimated_cost_usd: 0.0353

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 305
- http_status: 200

### Api Availability
- Score: 100
- features: ['openapi_spec', 'graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://anchor.fm/swagger.json', 'https://anchor.fm/graphql', 'https://api.anchor.fm', 'https://anchor.fm/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.