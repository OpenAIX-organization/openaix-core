# OpenAIX Evaluation Report

**Target**: https://pcmag.com
**Score**: 45/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-24T19:15:28Z
**Site Type**: platform (confidence: 33%)

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
- Score: 34
- snr_percent: 6.07
- raw_tokens: 203910
- clean_tokens: 12383

### Semantic
- Score: 90
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 52
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 12383
- estimated_cost_usd: 0.3715

### Permissions
- Score: 40
- allowed_agents: ['Google-Extended']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 57
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