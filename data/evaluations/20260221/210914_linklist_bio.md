# OpenAIX Evaluation Report

**Target**: https://linklist.bio
**Score**: 51/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-21T13:09:14Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 8
- snr_percent: 1.3
- raw_tokens: 190895
- clean_tokens: 2490

### Semantic
- Score: 66
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 13
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2490
- estimated_cost_usd: 0.0747

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 144
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.linklist.bio']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.