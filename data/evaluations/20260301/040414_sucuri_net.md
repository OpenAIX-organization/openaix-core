# OpenAIX Evaluation Report

**Target**: https://sucuri.net/waf
**Score**: 46/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-28T20:04:14Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 6%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 34
- snr_percent: 6.07
- raw_tokens: 38520
- clean_tokens: 2340

### Semantic
- Score: 57
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 5
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2340
- estimated_cost_usd: 0.0702

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 585
- http_status: 404

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