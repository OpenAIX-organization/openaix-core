# OpenAIX Evaluation Report

**Target**: https://corriere.it
**Score**: 51/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T22:06:15Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 30%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 86
- snr_percent: 30.43
- raw_tokens: 259940
- clean_tokens: 79094

### Semantic
- Score: 94
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 236
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 79094
- estimated_cost_usd: 2.3728

### Permissions
- Score: 50
- allowed_agents: ['ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 172
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