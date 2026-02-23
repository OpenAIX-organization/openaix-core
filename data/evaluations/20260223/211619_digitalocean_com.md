# OpenAIX Evaluation Report

**Target**: https://digitalocean.com
**Score**: 57/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-23T13:16:19Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 9%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 47
- snr_percent: 9.32
- raw_tokens: 90374
- clean_tokens: 8425

### Semantic
- Score: 59
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 47
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8425
- estimated_cost_usd: 0.2528

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 162
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.digitalocean.com', 'https://digitalocean.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.