# OpenAIX Evaluation Report

**Target**: https://disqus.com
**Score**: 39/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T16:09:24Z
**Site Type**: documentation (confidence: 0%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 6
- snr_percent: 1.03
- raw_tokens: 1649
- clean_tokens: 17

### Semantic
- Score: 15
- semantic_tags_used: []
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 17
- estimated_cost_usd: 0.0005

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 2
- http_status: 200

### Api Availability
- Score: 35
- features: ['api_subdomain', 'api_docs']
- endpoints_found: ['https://api.disqus.com', 'https://disqus.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.