# OpenAIX Evaluation Report

**Target**: https://buzzfeed.com
**Score**: 39/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T18:13:30Z
**Site Type**: documentation (confidence: 50%)

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
- snr_percent: 0.67
- raw_tokens: 603139
- clean_tokens: 4026

### Semantic
- Score: 56
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside']
- json_ld_present: False
- hidden_gem: False
- images_total: 8
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4026
- estimated_cost_usd: 0.1208

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 57
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