# OpenAIX Evaluation Report

**Target**: https://andersnoren.se
**Score**: 63/100
**Grade**: Class A (Agent Friendly)
**Timestamp**: 2026-03-01T12:06:28Z
**Site Type**: content (confidence: 100%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 20
- snr_percent: 3.37
- raw_tokens: 36337
- clean_tokens: 1223

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 2
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1223
- estimated_cost_usd: 0.0367

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 13
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.