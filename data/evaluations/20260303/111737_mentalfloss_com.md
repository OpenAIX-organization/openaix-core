# OpenAIX Evaluation Report

**Target**: https://mentalfloss.com
**Score**: 53/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-03-03T03:17:37Z
**Site Type**: product (confidence: 36%)

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
- snr_percent: 4.19
- raw_tokens: 176408
- clean_tokens: 7399

### Semantic
- Score: 74
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 42
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 7399
- estimated_cost_usd: 0.222

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 79
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