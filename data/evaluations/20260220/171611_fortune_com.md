# OpenAIX Evaluation Report

**Target**: https://fortune.com
**Score**: 39/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-20T09:16:11Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 9
- snr_percent: 1.53
- raw_tokens: 1210800
- clean_tokens: 18512

### Semantic
- Score: 74
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 72
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 18512
- estimated_cost_usd: 0.5554

### Permissions
- Score: 80
- allowed_agents: ['GPTBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['CCBot', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 18
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
- 📝 Add /llms.txt to describe your site for AI agents.