# OpenAIX Evaluation Report

**Target**: https://haaretz.com
**Score**: 38/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-28T11:07:55Z
**Site Type**: content (confidence: 46%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 27
- snr_percent: 4.53
- raw_tokens: 614598
- clean_tokens: 27815

### Semantic
- Score: 64
- semantic_tags_used: ['article', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 81
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 27815
- estimated_cost_usd: 0.8345

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 53
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