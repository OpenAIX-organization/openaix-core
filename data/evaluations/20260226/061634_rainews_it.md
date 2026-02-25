# OpenAIX Evaluation Report

**Target**: https://rainews.it
**Score**: 47/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T22:16:34Z
**Site Type**: content (confidence: 100%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 3
- snr_percent: 0.42
- raw_tokens: 634043
- clean_tokens: 2653

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 4
- heading_levels: 1
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2653
- estimated_cost_usd: 0.0796

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 251
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
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.