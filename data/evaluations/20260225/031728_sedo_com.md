# OpenAIX Evaluation Report

**Target**: https://sedo.com
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-24T19:17:28Z
**Site Type**: product (confidence: 50%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 20
- snr_percent: 3.35
- raw_tokens: 46928
- clean_tokens: 1574

### Semantic
- Score: 39
- semantic_tags_used: ['main']
- json_ld_present: False
- hidden_gem: False
- images_total: 5
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1574
- estimated_cost_usd: 0.0472

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 818
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.sedo.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.