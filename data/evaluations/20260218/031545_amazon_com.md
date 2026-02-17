# OpenAIX Evaluation Report

**Target**: https://amazon.com
**Score**: 39/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T19:15:45Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 11%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 52
- snr_percent: 11.14
- raw_tokens: 287996
- clean_tokens: 32095

### Semantic
- Score: 42
- semantic_tags_used: ['nav', 'header']
- json_ld_present: False
- hidden_gem: False
- images_total: 109
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 32095
- estimated_cost_usd: 0.9628

### Permissions
- Score: 40
- allowed_agents: ['anthropic-ai']
- blocked_agents: ['GPTBot', 'CCBot', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 693
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.amazon.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.