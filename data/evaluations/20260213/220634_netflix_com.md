# OpenAIX Evaluation Report

**Target**: https://netflix.com
**Score**: 52/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T14:06:34Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 0
- snr_percent: 0.07
- raw_tokens: 1540768
- clean_tokens: 1132

### Semantic
- Score: 47
- semantic_tags_used: ['header', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1132
- estimated_cost_usd: 0.034

### Permissions
- Score: 80
- allowed_agents: ['GPTBot', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['CCBot', 'anthropic-ai']
- llms_txt_present: True
- response_time_ms: 578
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://netflix.com/graphql', 'https://netflix.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.