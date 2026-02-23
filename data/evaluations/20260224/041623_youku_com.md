# OpenAIX Evaluation Report

**Target**: https://youku.com
**Score**: 39/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-23T20:16:23Z
**Site Type**: documentation (confidence: 0%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 28
- snr_percent: 4.61
- raw_tokens: 422342
- clean_tokens: 19480

### Semantic
- Score: 15
- semantic_tags_used: []
- json_ld_present: False
- hidden_gem: False
- images_total: 184
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 19480
- estimated_cost_usd: 0.5844

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 1424
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://youku.com/graphql', 'https://api.youku.com', 'https://youku.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.