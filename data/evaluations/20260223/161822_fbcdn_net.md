# OpenAIX Evaluation Report

**Target**: https://fbcdn.net
**Score**: 51/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-23T08:18:22Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 7
- snr_percent: 1.09
- raw_tokens: 166343
- clean_tokens: 1816

### Semantic
- Score: 8
- semantic_tags_used: []
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1816
- estimated_cost_usd: 0.0545

### Permissions
- Score: 80
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: True
- response_time_ms: 307
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://fbcdn.net/graphql', 'https://api.fbcdn.net', 'https://fbcdn.net/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.