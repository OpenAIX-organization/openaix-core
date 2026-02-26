# OpenAIX Evaluation Report

**Target**: https://printfriendly.com
**Score**: 52/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T11:15:15Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 8
- snr_percent: 1.36
- raw_tokens: 201909
- clean_tokens: 2755

### Semantic
- Score: 71
- semantic_tags_used: ['header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 24
- heading_levels: 4
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2755
- estimated_cost_usd: 0.0826

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 252
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.printfriendly.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.