# OpenAIX Evaluation Report

**Target**: https://nytimes.com
**Score**: 43/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T22:17:29Z
**Site Type**: platform (confidence: 36%)

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
- snr_percent: 1.22
- raw_tokens: 458730
- clean_tokens: 5609

### Semantic
- Score: 92
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 60
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 5609
- estimated_cost_usd: 0.1683

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 174
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