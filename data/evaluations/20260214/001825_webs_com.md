# OpenAIX Evaluation Report

**Target**: https://webs.com
**Score**: 64/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T16:18:25Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 17
- snr_percent: 2.8
- raw_tokens: 72774
- clean_tokens: 2035

### Semantic
- Score: 57
- semantic_tags_used: ['article', 'nav', 'header', 'main']
- json_ld_present: False
- hidden_gem: False
- images_total: 29
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2035
- estimated_cost_usd: 0.0611

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 100
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://webs.com/graphql', 'https://api.webs.com', 'https://webs.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.