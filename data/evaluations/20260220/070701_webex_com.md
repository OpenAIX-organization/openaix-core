# OpenAIX Evaluation Report

**Target**: https://webex.com
**Score**: 49/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-19T23:07:01Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 18%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 67
- snr_percent: 18.32
- raw_tokens: 35637
- clean_tokens: 6528

### Semantic
- Score: 36
- semantic_tags_used: ['header', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 41
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6528
- estimated_cost_usd: 0.1958

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 50
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.webex.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.