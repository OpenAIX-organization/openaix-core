# OpenAIX Evaluation Report

**Target**: https://citynews.ca
**Score**: 64/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-03-02T18:05:01Z
**Site Type**: content (confidence: 100%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['graphql', 'api_docs']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 13
- snr_percent: 2.12
- raw_tokens: 9007
- clean_tokens: 191

### Semantic
- Score: 85
- semantic_tags_used: []
- json_ld_present: True
- hidden_gem: True
- images_total: 1
- heading_levels: 1
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 191
- estimated_cost_usd: 0.0057

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 20
- http_status: 200

### Api Availability
- Score: 40
- features: ['graphql', 'api_docs']
- endpoints_found: ['https://citynews.ca/graphql', 'https://citynews.ca/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.