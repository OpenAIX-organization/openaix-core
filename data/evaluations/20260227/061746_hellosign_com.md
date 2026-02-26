# OpenAIX Evaluation Report

**Target**: https://hellosign.com
**Score**: 64/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T22:17:46Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 19%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 68
- snr_percent: 18.83
- raw_tokens: 31477
- clean_tokens: 5926

### Semantic
- Score: 63
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 76
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 5926
- estimated_cost_usd: 0.1778

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 338
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.hellosign.com', 'https://hellosign.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.