# OpenAIX Evaluation Report

**Target**: https://laravel.com
**Score**: 46/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T12:13:52Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 1%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 9
- snr_percent: 1.45
- raw_tokens: 548053
- clean_tokens: 7965

### Semantic
- Score: 37
- semantic_tags_used: ['nav']
- json_ld_present: False
- hidden_gem: False
- images_total: 45
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 7965
- estimated_cost_usd: 0.2389

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 70
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.laravel.com', 'https://laravel.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.