# OpenAIX Evaluation Report

**Target**: https://yandex.com
**Score**: 39/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-23T16:15:37Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 1
- snr_percent: 0.19
- raw_tokens: 134769
- clean_tokens: 256

### Semantic
- Score: 22
- semantic_tags_used: ['nav', 'main']
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 256
- estimated_cost_usd: 0.0077

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 420
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.yandex.com', 'https://yandex.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.