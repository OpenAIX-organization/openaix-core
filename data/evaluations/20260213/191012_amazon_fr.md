# OpenAIX Evaluation Report

**Target**: https://amazon.fr
**Score**: 40/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T11:10:12Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 14%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 58
- snr_percent: 13.95
- raw_tokens: 257254
- clean_tokens: 35895

### Semantic
- Score: 42
- semantic_tags_used: ['nav', 'header']
- json_ld_present: False
- hidden_gem: False
- images_total: 127
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 35895
- estimated_cost_usd: 1.0769

### Permissions
- Score: 40
- allowed_agents: ['anthropic-ai']
- blocked_agents: ['GPTBot', 'CCBot', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 843
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.amazon.fr']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.