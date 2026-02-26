# OpenAIX Evaluation Report

**Target**: https://tally.so
**Score**: 68/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T16:16:41Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['openapi_spec', 'api_subdomain', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 22
- snr_percent: 3.71
- raw_tokens: 80649
- clean_tokens: 2995

### Semantic
- Score: 85
- semantic_tags_used: ['header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 51
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2995
- estimated_cost_usd: 0.0898

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 376
- http_status: 200

### Api Availability
- Score: 60
- features: ['openapi_spec', 'api_subdomain', 'cli_tool']
- endpoints_found: ['https://tally.so/api/openapi.json', 'https://api.tally.so']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.