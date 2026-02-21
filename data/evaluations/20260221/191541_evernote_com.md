# OpenAIX Evaluation Report

**Target**: https://evernote.com
**Score**: 51/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-21T11:15:41Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 18
- snr_percent: 3.05
- raw_tokens: 110688
- clean_tokens: 3375

### Semantic
- Score: 62
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 63
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3375
- estimated_cost_usd: 0.1012

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 98
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.evernote.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.