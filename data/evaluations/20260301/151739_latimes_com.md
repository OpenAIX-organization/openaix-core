# OpenAIX Evaluation Report

**Target**: https://latimes.com/books
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T07:17:39Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 6%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 36
- snr_percent: 6.5
- raw_tokens: 220655
- clean_tokens: 14335

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 44
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 14335
- estimated_cost_usd: 0.43

### Permissions
- Score: 80
- allowed_agents: ['CCBot', 'anthropic-ai', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'ClaudeBot']
- llms_txt_present: False
- response_time_ms: 43
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.