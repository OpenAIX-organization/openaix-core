# OpenAIX Evaluation Report

**Target**: https://yandex.ru
**Score**: 32/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T12:15:22Z
**Site Type**: documentation (confidence: 0%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 2
- snr_percent: 0.34
- raw_tokens: 1298692
- clean_tokens: 4358

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
- clean_tokens: 4358
- estimated_cost_usd: 0.1307

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 1128
- http_status: 200

### Api Availability
- Score: 35
- features: ['api_subdomain', 'api_docs']
- endpoints_found: ['https://api.yandex.ru', 'https://yandex.ru/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.