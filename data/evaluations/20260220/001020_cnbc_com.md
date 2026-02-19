# OpenAIX Evaluation Report

**Target**: https://cnbc.com
**Score**: 42/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-19T16:10:20Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 15
- snr_percent: 2.55
- raw_tokens: 360773
- clean_tokens: 9191

### Semantic
- Score: 71
- semantic_tags_used: ['header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 11
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 9191
- estimated_cost_usd: 0.2757

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 116
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.cnbc.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.