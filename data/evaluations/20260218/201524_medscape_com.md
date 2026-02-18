# OpenAIX Evaluation Report

**Target**: https://medscape.com
**Score**: 43/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T12:15:24Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 10%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 49
- snr_percent: 9.74
- raw_tokens: 81427
- clean_tokens: 7927

### Semantic
- Score: 66
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 47
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 7927
- estimated_cost_usd: 0.2378

### Permissions
- Score: 60
- allowed_agents: ['anthropic-ai', 'ChatGPT-User', 'Google-Extended']
- blocked_agents: ['GPTBot', 'CCBot', 'ClaudeBot', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 48
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.