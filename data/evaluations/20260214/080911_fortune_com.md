# OpenAIX Evaluation Report

**Target**: https://fortune.com
**Score**: 44/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-14T00:09:11Z
**Site Type**: product (confidence: 33%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 10
- snr_percent: 1.6
- raw_tokens: 1213000
- clean_tokens: 19387

### Semantic
- Score: 74
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 72
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 19387
- estimated_cost_usd: 0.5816

### Permissions
- Score: 80
- allowed_agents: ['GPTBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['CCBot', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 23
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