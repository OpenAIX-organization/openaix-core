# OpenAIX Evaluation Report

**Target**: https://site.com
**Score**: 56/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T10:15:23Z
**Site Type**: platform (confidence: 41%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 20
- snr_percent: 3.25
- raw_tokens: 158206
- clean_tokens: 5142

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section']
- json_ld_present: True
- hidden_gem: True
- images_total: 190
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 5142
- estimated_cost_usd: 0.1543

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 301
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://site.com/docs/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.