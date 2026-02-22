# OpenAIX Evaluation Report

**Target**: https://alibaba.com
**Score**: 50/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T14:06:58Z
**Site Type**: product (confidence: 36%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 29
- snr_percent: 4.82
- raw_tokens: 45311
- clean_tokens: 2186

### Semantic
- Score: 32
- semantic_tags_used: ['nav', 'section']
- json_ld_present: True
- hidden_gem: False
- images_total: 27
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2186
- estimated_cost_usd: 0.0656

### Permissions
- Score: 80
- allowed_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'Google-Extended']
- llms_txt_present: True
- response_time_ms: 318
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://alibaba.com/graphql', 'https://api.alibaba.com', 'https://alibaba.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.