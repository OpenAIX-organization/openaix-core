# OpenAIX Evaluation Report

**Target**: https://cowboy.com
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T05:18:10Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 10
- snr_percent: 1.6
- raw_tokens: 281152
- clean_tokens: 4502

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 76
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4502
- estimated_cost_usd: 0.1351

### Permissions
- Score: 95
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 1511
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.