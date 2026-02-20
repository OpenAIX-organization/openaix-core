# OpenAIX Evaluation Report

**Target**: https://salon.com
**Score**: 62/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-20T01:17:03Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 27%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 81
- snr_percent: 27.28
- raw_tokens: 32496
- clean_tokens: 8864

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 38
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8864
- estimated_cost_usd: 0.2659

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 16
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://salon.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.