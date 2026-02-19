# OpenAIX Evaluation Report

**Target**: https://buzzfeed.com
**Score**: 39/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-19T06:10:27Z
**Site Type**: documentation (confidence: 33%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['openapi_spec', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 4
- snr_percent: 0.66
- raw_tokens: 611143
- clean_tokens: 4043

### Semantic
- Score: 55
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside']
- json_ld_present: False
- hidden_gem: False
- images_total: 9
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4043
- estimated_cost_usd: 0.1213

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 48
- http_status: 200

### Api Availability
- Score: 40
- features: ['openapi_spec', 'cli_tool']
- endpoints_found: ['https://buzzfeed.com/swagger.json']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.