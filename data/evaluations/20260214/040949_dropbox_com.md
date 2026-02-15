# OpenAIX Evaluation Report

**Target**: https://dropbox.com
**Score**: 53/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T20:09:49Z
**Site Type**: platform (confidence: 38%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 21
- snr_percent: 3.44
- raw_tokens: 211987
- clean_tokens: 7287

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'main', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 78
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 7287
- estimated_cost_usd: 0.2186

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 621
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://dropbox.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.