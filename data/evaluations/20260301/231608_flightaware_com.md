# OpenAIX Evaluation Report

**Target**: https://flightaware.com
**Score**: 50/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T15:16:08Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 47%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 100
- snr_percent: 46.71
- raw_tokens: 49640
- clean_tokens: 23185

### Semantic
- Score: 46
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 7
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 23185
- estimated_cost_usd: 0.6955

### Permissions
- Score: 90
- allowed_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot']
- llms_txt_present: False
- response_time_ms: 155
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://flightaware.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.