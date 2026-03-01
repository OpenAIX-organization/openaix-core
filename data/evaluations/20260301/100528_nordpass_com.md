# OpenAIX Evaluation Report

**Target**: https://nordpass.com
**Score**: 59/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T02:05:28Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 24
- snr_percent: 3.97
- raw_tokens: 106378
- clean_tokens: 4221

### Semantic
- Score: 67
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 27
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4221
- estimated_cost_usd: 0.1266

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 314
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.nordpass.com', 'https://nordpass.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.