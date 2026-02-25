# OpenAIX Evaluation Report

**Target**: https://nouvelobs.com
**Score**: 53/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T23:07:52Z
**Site Type**: platform (confidence: 50%)

---

## Metrics

- **snr**: 12%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 55
- snr_percent: 12.34
- raw_tokens: 50627
- clean_tokens: 6248

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 9
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6248
- estimated_cost_usd: 0.1874

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 6
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.nouvelobs.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.