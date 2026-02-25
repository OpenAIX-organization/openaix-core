# OpenAIX Evaluation Report

**Target**: https://elasticEmail.com
**Score**: 71/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T16:06:06Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 15
- snr_percent: 2.57
- raw_tokens: 136578
- clean_tokens: 3511

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'section']
- json_ld_present: True
- hidden_gem: True
- images_total: 66
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3511
- estimated_cost_usd: 0.1053

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 583
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://elasticEmail.com/graphql', 'https://api.elasticEmail.com', 'https://elasticEmail.com/developers']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.