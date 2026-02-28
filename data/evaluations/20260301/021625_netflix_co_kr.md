# OpenAIX Evaluation Report

**Target**: https://netflix.co.kr
**Score**: 44/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-28T18:16:25Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 0
- snr_percent: 0.07
- raw_tokens: 1540997
- clean_tokens: 1129

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
- clean_tokens: 1129
- estimated_cost_usd: 0.0339

### Permissions
- Score: 80
- allowed_agents: ['GPTBot', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['CCBot', 'anthropic-ai']
- llms_txt_present: True
- response_time_ms: 651
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://netflix.co.kr/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.