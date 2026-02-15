# OpenAIX Evaluation Report

**Target**: https://vkontakte.ru
**Score**: 46/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-14T12:17:54Z
**Site Type**: platform (confidence: 100%)

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
- snr_percent: 0.02
- raw_tokens: 39117
- clean_tokens: 6

### Semantic
- Score: 15
- semantic_tags_used: []
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 6
- estimated_cost_usd: 0.0002

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 883
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://vkontakte.ru/graphql', 'https://vkontakte.ru/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.