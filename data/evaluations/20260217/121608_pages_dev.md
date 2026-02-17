# OpenAIX Evaluation Report

**Target**: https://pages.dev
**Score**: 62/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T04:16:08Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 20
- snr_percent: 3.4
- raw_tokens: 44991
- clean_tokens: 1528

### Semantic
- Score: 68
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 3
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1528
- estimated_cost_usd: 0.0458

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 26
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://pages.dev/graphql', 'https://pages.dev/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.