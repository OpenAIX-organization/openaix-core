# OpenAIX Evaluation Report

**Target**: https://behance.net
**Score**: 43/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T12:12:23Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 16
- snr_percent: 2.65
- raw_tokens: 299109
- clean_tokens: 7939

### Semantic
- Score: 61
- semantic_tags_used: ['nav', 'main', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 68
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 7939
- estimated_cost_usd: 0.2382

### Permissions
- Score: 50
- allowed_agents: ['ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 48
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.behance.net']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.