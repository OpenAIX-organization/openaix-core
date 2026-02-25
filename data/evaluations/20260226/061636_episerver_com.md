# OpenAIX Evaluation Report

**Target**: https://episerver.com
**Score**: 62/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-25T22:16:36Z
**Site Type**: product (confidence: 33%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 17
- snr_percent: 2.9
- raw_tokens: 114576
- clean_tokens: 3317

### Semantic
- Score: 81
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 24
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3317
- estimated_cost_usd: 0.0995

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 375
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.episerver.com', 'https://episerver.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.