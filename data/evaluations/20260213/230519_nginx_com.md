# OpenAIX Evaluation Report

**Target**: https://nginx.com
**Score**: 54/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T15:05:19Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 21
- snr_percent: 3.56
- raw_tokens: 131988
- clean_tokens: 4702

### Semantic
- Score: 43
- semantic_tags_used: ['nav', 'section']
- json_ld_present: False
- hidden_gem: False
- images_total: 3
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4702
- estimated_cost_usd: 0.1411

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 611
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://nginx.com/graphql', 'https://nginx.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.