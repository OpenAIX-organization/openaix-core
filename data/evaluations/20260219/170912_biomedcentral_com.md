# OpenAIX Evaluation Report

**Target**: https://biomedcentral.com
**Score**: 59/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-19T09:09:12Z
**Site Type**: product (confidence: 33%)

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
- Score: 25
- snr_percent: 4.14
- raw_tokens: 86056
- clean_tokens: 3561

### Semantic
- Score: 71
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 10
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3561
- estimated_cost_usd: 0.1068

### Permissions
- Score: 80
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: True
- response_time_ms: 440
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://biomedcentral.com/graphql', 'https://biomedcentral.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.