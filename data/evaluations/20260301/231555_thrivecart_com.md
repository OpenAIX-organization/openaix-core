# OpenAIX Evaluation Report

**Target**: https://thrivecart.com
**Score**: 70/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T15:15:55Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 5%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 27
- snr_percent: 4.52
- raw_tokens: 326083
- clean_tokens: 14734

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 202
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 14734
- estimated_cost_usd: 0.442

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 141
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://thrivecart.com/graphql', 'https://api.thrivecart.com', 'https://thrivecart.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.