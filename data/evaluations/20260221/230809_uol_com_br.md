# OpenAIX Evaluation Report

**Target**: https://uol.com.br
**Score**: 50/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-21T15:08:09Z
**Site Type**: platform (confidence: 54%)

---

## Metrics

- **snr**: 16%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 61
- snr_percent: 15.5
- raw_tokens: 253275
- clean_tokens: 39246

### Semantic
- Score: 86
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 195
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 39246
- estimated_cost_usd: 1.1774

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 191
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.uol.com.br']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.