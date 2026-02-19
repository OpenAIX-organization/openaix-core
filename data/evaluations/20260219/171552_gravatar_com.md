# OpenAIX Evaluation Report

**Target**: https://gravatar.com
**Score**: 49/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-19T09:15:52Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 25
- snr_percent: 4.13
- raw_tokens: 40444
- clean_tokens: 1671

### Semantic
- Score: 55
- semantic_tags_used: ['nav', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 19
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1671
- estimated_cost_usd: 0.0501

### Permissions
- Score: 80
- allowed_agents: ['anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'Google-Extended']
- llms_txt_present: True
- response_time_ms: 52
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://gravatar.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.