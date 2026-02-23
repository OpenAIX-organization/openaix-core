# OpenAIX Evaluation Report

**Target**: https://nike.com
**Score**: 54/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-23T23:11:54Z
**Site Type**: product (confidence: 34%)

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
- Score: 28
- snr_percent: 4.74
- raw_tokens: 323898
- clean_tokens: 15349

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 53
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 15349
- estimated_cost_usd: 0.4605

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 592
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