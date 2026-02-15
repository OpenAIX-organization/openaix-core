# OpenAIX Evaluation Report

**Target**: https://yahoo.com
**Score**: 36/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T21:19:32Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 7
- snr_percent: 1.18
- raw_tokens: 249812
- clean_tokens: 2947

### Semantic
- Score: 61
- semantic_tags_used: ['article', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 16
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2947
- estimated_cost_usd: 0.0884

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 959
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.