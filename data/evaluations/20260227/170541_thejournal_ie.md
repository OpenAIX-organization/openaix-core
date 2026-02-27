# OpenAIX Evaluation Report

**Target**: https://thejournal.ie
**Score**: 42/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-27T09:05:41Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 17
- snr_percent: 2.88
- raw_tokens: 220378
- clean_tokens: 6349

### Semantic
- Score: 46
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 79
- heading_levels: 1
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6349
- estimated_cost_usd: 0.1905

### Permissions
- Score: 80
- allowed_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'ChatGPT-User']
- llms_txt_present: False
- response_time_ms: 423
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.thejournal.ie']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.