# OpenAIX Evaluation Report

**Target**: https://wikia.com
**Score**: 50/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T09:15:24Z
**Site Type**: product (confidence: 58%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 8
- snr_percent: 1.41
- raw_tokens: 333436
- clean_tokens: 4704

### Semantic
- Score: 42
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 43
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4704
- estimated_cost_usd: 0.1411

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 98
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://wikia.com/graphql', 'https://api.wikia.com', 'https://wikia.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.