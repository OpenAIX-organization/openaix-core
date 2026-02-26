# OpenAIX Evaluation Report

**Target**: https://amtrak.com
**Score**: 56/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T04:04:15Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 8%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 44
- snr_percent: 8.44
- raw_tokens: 62227
- clean_tokens: 5254

### Semantic
- Score: 64
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 24
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 5254
- estimated_cost_usd: 0.1576

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 54
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.amtrak.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.