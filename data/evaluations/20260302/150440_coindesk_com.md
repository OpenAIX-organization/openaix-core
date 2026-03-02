# OpenAIX Evaluation Report

**Target**: https://coindesk.com
**Score**: 42/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T07:04:40Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 15
- snr_percent: 2.57
- raw_tokens: 339608
- clean_tokens: 8716

### Semantic
- Score: 53
- semantic_tags_used: ['nav', 'header', 'main', 'aside', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 28
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8716
- estimated_cost_usd: 0.2615

### Permissions
- Score: 80
- allowed_agents: ['ChatGPT-User']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: True
- response_time_ms: 379
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://coindesk.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.