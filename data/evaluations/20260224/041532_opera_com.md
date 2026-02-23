# OpenAIX Evaluation Report

**Target**: https://opera.com
**Score**: 64/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-23T20:15:32Z
**Site Type**: product (confidence: 41%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 26
- snr_percent: 4.33
- raw_tokens: 69436
- clean_tokens: 3007

### Semantic
- Score: 89
- semantic_tags_used: ['header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 36
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3007
- estimated_cost_usd: 0.0902

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 214
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://opera.com/docs/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.