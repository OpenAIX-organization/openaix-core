# OpenAIX Evaluation Report

**Target**: https://theprint.in
**Score**: 53/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T08:09:13Z
**Site Type**: product (confidence: 36%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 19
- snr_percent: 3.12
- raw_tokens: 320231
- clean_tokens: 10005

### Semantic
- Score: 85
- semantic_tags_used: ['header', 'aside']
- json_ld_present: True
- hidden_gem: True
- images_total: 24
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 10005
- estimated_cost_usd: 0.3002

### Permissions
- Score: 70
- allowed_agents: ['anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 1411
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.