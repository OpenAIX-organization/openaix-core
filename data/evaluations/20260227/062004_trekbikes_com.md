# OpenAIX Evaluation Report

**Target**: https://trekbikes.com
**Score**: 50/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T22:20:04Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 4
- snr_percent: 0.7
- raw_tokens: 72851
- clean_tokens: 510

### Semantic
- Score: 54
- semantic_tags_used: ['article', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 510
- estimated_cost_usd: 0.0153

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 1426
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.trekbikes.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.