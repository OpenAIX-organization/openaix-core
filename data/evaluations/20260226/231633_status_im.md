# OpenAIX Evaluation Report

**Target**: https://status.im
**Score**: 55/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T15:16:33Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 8
- snr_percent: 1.29
- raw_tokens: 233060
- clean_tokens: 3002

### Semantic
- Score: 53
- semantic_tags_used: ['nav', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 33
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3002
- estimated_cost_usd: 0.0901

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 42
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://status.im/graphql', 'https://status.im/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.