# OpenAIX Evaluation Report

**Target**: https://desmoinesregister.com
**Score**: 41/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-28T09:15:31Z
**Site Type**: documentation (confidence: 26%)

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
- Score: 27
- snr_percent: 4.48
- raw_tokens: 82894
- clean_tokens: 3712

### Semantic
- Score: 33
- semantic_tags_used: ['nav', 'header', 'main', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 35
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3712
- estimated_cost_usd: 0.1114

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 78
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.desmoinesregister.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.