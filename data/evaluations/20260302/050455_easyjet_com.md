# OpenAIX Evaluation Report

**Target**: https://easyjet.com
**Score**: 70/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T21:04:55Z
**Site Type**: platform (confidence: 33%)

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
- raw_tokens: 226443
- clean_tokens: 10229

### Semantic
- Score: 88
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 53
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 10229
- estimated_cost_usd: 0.3069

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 312
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://easyjet.com/graphql', 'https://api.easyjet.com', 'https://easyjet.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.