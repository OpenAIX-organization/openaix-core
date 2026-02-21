# OpenAIX Evaluation Report

**Target**: https://amazon.co.uk
**Score**: 39/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-21T07:10:58Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 12%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 55
- snr_percent: 12.49
- raw_tokens: 273672
- clean_tokens: 34193

### Semantic
- Score: 42
- semantic_tags_used: ['nav', 'header']
- json_ld_present: False
- hidden_gem: False
- images_total: 119
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 34193
- estimated_cost_usd: 1.0258

### Permissions
- Score: 40
- allowed_agents: ['anthropic-ai']
- blocked_agents: ['GPTBot', 'CCBot', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 700
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.amazon.co.uk']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.