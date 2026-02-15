# OpenAIX Evaluation Report

**Target**: https://paypal.com
**Score**: 58/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-14T21:15:25Z
**Site Type**: platform (confidence: 41%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 19
- snr_percent: 3.16
- raw_tokens: 85052
- clean_tokens: 2685

### Semantic
- Score: 59
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 2
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2685
- estimated_cost_usd: 0.0805

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 370
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://paypal.com/graphql', 'https://paypal.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.