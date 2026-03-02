# OpenAIX Evaluation Report

**Target**: https://recurly.com
**Score**: 70/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T20:16:18Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 10
- snr_percent: 1.69
- raw_tokens: 248429
- clean_tokens: 4207

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 66
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4207
- estimated_cost_usd: 0.1262

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 85
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://recurly.com/graphql', 'https://api.recurly.com', 'https://recurly.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.