# OpenAIX Evaluation Report

**Target**: https://facebook.com
**Score**: 56/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T11:16:00Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 24
- snr_percent: 4.0
- raw_tokens: 31272
- clean_tokens: 1252

### Semantic
- Score: 20
- semantic_tags_used: []
- json_ld_present: False
- hidden_gem: False
- images_total: 2
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1252
- estimated_cost_usd: 0.0376

### Permissions
- Score: 80
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: True
- response_time_ms: 267
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://facebook.com/graphql', 'https://api.facebook.com', 'https://facebook.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.