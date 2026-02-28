# OpenAIX Evaluation Report

**Target**: https://packer.io
**Score**: 60/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-28T11:07:30Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 24
- snr_percent: 3.96
- raw_tokens: 34709
- clean_tokens: 1375

### Semantic
- Score: 54
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 3
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1375
- estimated_cost_usd: 0.0412

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 125
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://packer.io/graphql', 'https://packer.io/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.