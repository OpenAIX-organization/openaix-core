# OpenAIX Evaluation Report

**Target**: https://hootsuite.com
**Score**: 57/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T12:13:33Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 6%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 34
- snr_percent: 5.88
- raw_tokens: 172549
- clean_tokens: 10138

### Semantic
- Score: 64
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 101
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 10138
- estimated_cost_usd: 0.3041

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 260
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.hootsuite.com', 'https://hootsuite.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📋 Add JSON-LD structured data for better AI understanding.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.