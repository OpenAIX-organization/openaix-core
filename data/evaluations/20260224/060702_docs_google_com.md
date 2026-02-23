# OpenAIX Evaluation Report

**Target**: https://docs.google.com
**Score**: 38/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-23T22:07:02Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 0
- snr_percent: 0.06
- raw_tokens: 511018
- clean_tokens: 329

### Semantic
- Score: 37
- semantic_tags_used: ['section']
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 1
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 329
- estimated_cost_usd: 0.0099

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 272
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.docs.google.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.