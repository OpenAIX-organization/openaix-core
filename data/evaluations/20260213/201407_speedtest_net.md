# OpenAIX Evaluation Report

**Target**: https://speedtest.net
**Score**: 41/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T12:14:07Z
**Site Type**: documentation (confidence: 50%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 8
- snr_percent: 1.4
- raw_tokens: 74661
- clean_tokens: 1048

### Semantic
- Score: 19
- semantic_tags_used: ['footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1048
- estimated_cost_usd: 0.0314

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 76
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.speedtest.net']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.