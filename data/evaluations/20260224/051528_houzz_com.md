# OpenAIX Evaluation Report

**Target**: https://houzz.com
**Score**: 51/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-23T21:15:28Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 2%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 13
- snr_percent: 2.11
- raw_tokens: 619151
- clean_tokens: 13055

### Semantic
- Score: 60
- semantic_tags_used: ['article', 'nav', 'header', 'section']
- json_ld_present: True
- hidden_gem: False
- images_total: 96
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 13055
- estimated_cost_usd: 0.3916

### Permissions
- Score: 90
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 3911
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.houzz.com', 'https://houzz.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.