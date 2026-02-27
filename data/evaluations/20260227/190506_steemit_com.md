# OpenAIX Evaluation Report

**Target**: https://steemit.com
**Score**: 62/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-27T11:05:06Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 4%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 26
- snr_percent: 4.27
- raw_tokens: 189834
- clean_tokens: 8102

### Semantic
- Score: 54
- semantic_tags_used: ['article', 'nav', 'header', 'aside']
- json_ld_present: False
- hidden_gem: False
- images_total: 19
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8102
- estimated_cost_usd: 0.2431

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 380
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://steemit.com/graphql', 'https://api.steemit.com', 'https://steemit.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.