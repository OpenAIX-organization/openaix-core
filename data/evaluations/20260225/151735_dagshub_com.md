# OpenAIX Evaluation Report

**Target**: https://dagshub.com
**Score**: 72/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T07:17:35Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 23
- snr_percent: 3.89
- raw_tokens: 65795
- clean_tokens: 2559

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'section']
- json_ld_present: True
- hidden_gem: True
- images_total: 55
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2559
- estimated_cost_usd: 0.0768

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 28
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://dagshub.com/graphql', 'https://api.dagshub.com', 'https://dagshub.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.