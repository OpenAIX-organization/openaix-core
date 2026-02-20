# OpenAIX Evaluation Report

**Target**: https://android.com
**Score**: 63/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-20T13:11:42Z
**Site Type**: product (confidence: 33%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 26
- snr_percent: 4.3
- raw_tokens: 72446
- clean_tokens: 3113

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 9
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3113
- estimated_cost_usd: 0.0934

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
- endpoints_found: ['https://android.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.