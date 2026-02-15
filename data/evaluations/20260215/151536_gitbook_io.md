# OpenAIX Evaluation Report

**Target**: https://gitbook.io
**Score**: 58/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-15T07:15:36Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 2%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 14
- snr_percent: 2.27
- raw_tokens: 481997
- clean_tokens: 10951

### Semantic
- Score: 48
- semantic_tags_used: ['section']
- json_ld_present: False
- hidden_gem: False
- images_total: 139
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 10951
- estimated_cost_usd: 0.3285

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 106
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://gitbook.io/graphql', 'https://api.gitbook.io', 'https://gitbook.io/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.