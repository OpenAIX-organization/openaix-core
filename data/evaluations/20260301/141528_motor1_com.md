# OpenAIX Evaluation Report

**Target**: https://motor1.com
**Score**: 58/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-03-01T06:15:28Z
**Site Type**: product (confidence: 45%)

---

## Metrics

- **snr**: 4%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 25
- snr_percent: 4.11
- raw_tokens: 217410
- clean_tokens: 8937

### Semantic
- Score: 98
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 60
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8937
- estimated_cost_usd: 0.2681

### Permissions
- Score: 60
- allowed_agents: ['GPTBot', 'ChatGPT-User', 'Google-Extended']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 146
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