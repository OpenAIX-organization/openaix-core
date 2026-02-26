# OpenAIX Evaluation Report

**Target**: https://nyse.com
**Score**: 47/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T11:16:00Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 15
- snr_percent: 2.58
- raw_tokens: 91897
- clean_tokens: 2374

### Semantic
- Score: 46
- semantic_tags_used: ['nav', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 15
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2374
- estimated_cost_usd: 0.0712

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 48
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.nyse.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.