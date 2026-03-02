# OpenAIX Evaluation Report

**Target**: https://plotly.com
**Score**: 55/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T03:03:34Z
**Site Type**: platform (confidence: 36%)

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
- Score: 17
- snr_percent: 2.8
- raw_tokens: 126767
- clean_tokens: 3545

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 47
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3545
- estimated_cost_usd: 0.1064

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 220
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://plotly.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.