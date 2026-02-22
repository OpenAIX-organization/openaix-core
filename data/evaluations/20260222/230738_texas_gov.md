# OpenAIX Evaluation Report

**Target**: https://texas.gov
**Score**: 59/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-22T15:07:38Z
**Site Type**: documentation (confidence: 70%)

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
- Score: 18
- snr_percent: 3.07
- raw_tokens: 54152
- clean_tokens: 1661

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 3
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1661
- estimated_cost_usd: 0.0498

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 73
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.