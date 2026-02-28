# OpenAIX Evaluation Report

**Target**: https://chime.aws
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-28T13:09:43Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 13
- snr_percent: 2.11
- raw_tokens: 76677
- clean_tokens: 1618

### Semantic
- Score: 51
- semantic_tags_used: ['nav', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 0
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1618
- estimated_cost_usd: 0.0485

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 147
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://chime.aws/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.