# OpenAIX Evaluation Report

**Target**: https://yandex.ru
**Score**: 31/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T19:16:06Z
**Site Type**: documentation (confidence: 0%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 2
- snr_percent: 0.41
- raw_tokens: 1007242
- clean_tokens: 4159

### Semantic
- Score: 33
- semantic_tags_used: ['article', 'header', 'main', 'section', 'aside']
- json_ld_present: False
- hidden_gem: False
- images_total: 7
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4159
- estimated_cost_usd: 0.1248

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 1180
- http_status: 200

### Api Availability
- Score: 20
- features: ['api_subdomain']
- endpoints_found: ['https://api.yandex.ru']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.