# OpenAIX Evaluation Report

**Target**: https://bsky.app
**Score**: 40/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T15:05:37Z
**Site Type**: documentation (confidence: 0%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 2
- snr_percent: 0.29
- raw_tokens: 2101
- clean_tokens: 6

### Semantic
- Score: 30
- semantic_tags_used: []
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 1
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 6
- estimated_cost_usd: 0.0002

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 60
- http_status: 200

### Api Availability
- Score: 20
- features: ['api_subdomain']
- endpoints_found: ['https://api.bsky.app']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.