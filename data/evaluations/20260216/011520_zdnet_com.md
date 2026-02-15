# OpenAIX Evaluation Report

**Target**: https://zdnet.com
**Score**: 30/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-15T17:15:20Z
**Site Type**: documentation (confidence: 26%)

---

## Metrics

- **snr**: 1%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 7
- snr_percent: 1.21
- raw_tokens: 559141
- clean_tokens: 6756

### Semantic
- Score: 39
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 9
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6756
- estimated_cost_usd: 0.2027

### Permissions
- Score: 40
- allowed_agents: ['Google-Extended']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 119
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.