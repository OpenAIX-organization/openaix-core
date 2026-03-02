# OpenAIX Evaluation Report

**Target**: https://sedaily.com
**Score**: 57/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T11:04:55Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 52%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 100
- snr_percent: 51.82
- raw_tokens: 72078
- clean_tokens: 37350

### Semantic
- Score: 71
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 96
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 37350
- estimated_cost_usd: 1.1205

### Permissions
- Score: 80
- allowed_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'ChatGPT-User']
- llms_txt_present: False
- response_time_ms: 430
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.sedaily.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.