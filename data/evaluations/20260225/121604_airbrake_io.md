# OpenAIX Evaluation Report

**Target**: https://airbrake.io
**Score**: 60/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T04:16:04Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 48%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 100
- snr_percent: 47.7
- raw_tokens: 23992
- clean_tokens: 11444

### Semantic
- Score: 37
- semantic_tags_used: ['nav']
- json_ld_present: False
- hidden_gem: False
- images_total: 201
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 11444
- estimated_cost_usd: 0.3433

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 148
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.airbrake.io', 'https://airbrake.io/docs/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.