# OpenAIX Evaluation Report

**Target**: https://openrouter.ai
**Score**: 71/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T21:07:44Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['openapi_spec', 'graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 28
- snr_percent: 4.68
- raw_tokens: 52759
- clean_tokens: 2471

### Semantic
- Score: 64
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 41
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2471
- estimated_cost_usd: 0.0741

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 100
- http_status: 200

### Api Availability
- Score: 80
- features: ['openapi_spec', 'graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://openrouter.ai/openapi.json', 'https://openrouter.ai/graphql', 'https://openrouter.ai/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.