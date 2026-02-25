# OpenAIX Evaluation Report

**Target**: https://ulta.com
**Score**: 47/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T13:15:45Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 29
- snr_percent: 4.79
- raw_tokens: 382176
- clean_tokens: 18312

### Semantic
- Score: 43
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 73
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 18312
- estimated_cost_usd: 0.5494

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 34
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.ulta.com', 'https://ulta.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.