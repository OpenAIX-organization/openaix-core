# OpenAIX Evaluation Report

**Target**: https://web.facebook.com
**Score**: 49/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T00:13:00Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 24
- snr_percent: 4.02
- raw_tokens: 31242
- clean_tokens: 1257

### Semantic
- Score: 20
- semantic_tags_used: []
- json_ld_present: False
- hidden_gem: False
- images_total: 2
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1257
- estimated_cost_usd: 0.0377

### Permissions
- Score: 80
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: True
- response_time_ms: 197
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://web.facebook.com/graphql', 'https://web.facebook.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.