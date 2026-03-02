# OpenAIX Evaluation Report

**Target**: https://ford.com
**Score**: 38/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T14:00:55Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 22
- snr_percent: 3.72
- raw_tokens: 469806
- clean_tokens: 17474

### Semantic
- Score: 61
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 249
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 17474
- estimated_cost_usd: 0.5242

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 159
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
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.