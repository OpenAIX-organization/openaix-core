# OpenAIX Evaluation Report

**Target**: https://amazon.com/appstore
**Score**: 41/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T03:03:13Z
**Site Type**: platform (confidence: 48%)

---

## Metrics

- **snr**: 8%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 44
- snr_percent: 8.45
- raw_tokens: 243385
- clean_tokens: 20578

### Semantic
- Score: 57
- semantic_tags_used: ['nav', 'header']
- json_ld_present: False
- hidden_gem: False
- images_total: 57
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 20578
- estimated_cost_usd: 0.6173

### Permissions
- Score: 40
- allowed_agents: ['anthropic-ai']
- blocked_agents: ['GPTBot', 'CCBot', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 665
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.amazon.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.