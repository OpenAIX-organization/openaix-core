# OpenAIX Evaluation Report

**Target**: https://airbnb.com
**Score**: 49/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-16T08:10:50Z
**Site Type**: content (confidence: 58%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 1
- snr_percent: 0.12
- raw_tokens: 182723
- clean_tokens: 223

### Semantic
- Score: 51
- semantic_tags_used: ['nav', 'header', 'main']
- json_ld_present: True
- hidden_gem: False
- images_total: 1
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 223
- estimated_cost_usd: 0.0067

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 536
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