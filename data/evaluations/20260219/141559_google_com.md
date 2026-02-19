# OpenAIX Evaluation Report

**Target**: https://google.com
**Score**: 31/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-19T06:15:59Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 1
- snr_percent: 0.24
- raw_tokens: 100850
- clean_tokens: 239

### Semantic
- Score: 18
- semantic_tags_used: []
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 239
- estimated_cost_usd: 0.0072

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 133
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://google.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.