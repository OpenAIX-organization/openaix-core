# OpenAIX Evaluation Report

**Target**: https://keycdn.com
**Score**: 52/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-27T13:15:30Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 23
- snr_percent: 3.87
- raw_tokens: 33208
- clean_tokens: 1285

### Semantic
- Score: 51
- semantic_tags_used: ['nav', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1285
- estimated_cost_usd: 0.0385

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 158
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.keycdn.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.