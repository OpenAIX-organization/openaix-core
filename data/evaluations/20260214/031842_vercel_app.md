# OpenAIX Evaluation Report

**Target**: https://vercel.app
**Score**: 65/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T19:18:42Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 7
- snr_percent: 1.15
- raw_tokens: 326099
- clean_tokens: 3758

### Semantic
- Score: 65
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 23
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3758
- estimated_cost_usd: 0.1127

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 111
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://vercel.app/graphql', 'https://api.vercel.app', 'https://vercel.app/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.