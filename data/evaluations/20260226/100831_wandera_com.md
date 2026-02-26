# OpenAIX Evaluation Report

**Target**: https://wandera.com
**Score**: 72/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T02:08:31Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 26
- snr_percent: 4.35
- raw_tokens: 101420
- clean_tokens: 4409

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 11
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4409
- estimated_cost_usd: 0.1323

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 89
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://wandera.com/graphql', 'https://api.wandera.com', 'https://wandera.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.