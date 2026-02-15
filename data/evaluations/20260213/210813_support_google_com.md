# OpenAIX Evaluation Report

**Target**: https://support.google.com
**Score**: 53/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T13:08:13Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 5
- snr_percent: 0.76
- raw_tokens: 483146
- clean_tokens: 3665

### Semantic
- Score: 47
- semantic_tags_used: ['article', 'header', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 21
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3665
- estimated_cost_usd: 0.1099

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 401
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://support.google.com/graphql', 'https://support.google.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.