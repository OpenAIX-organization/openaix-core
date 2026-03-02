# OpenAIX Evaluation Report

**Target**: https://siriusxm.com
**Score**: 50/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T22:01:21Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 22
- snr_percent: 3.65
- raw_tokens: 127522
- clean_tokens: 4651

### Semantic
- Score: 49
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 90
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4651
- estimated_cost_usd: 0.1395

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 100
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.siriusxm.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.