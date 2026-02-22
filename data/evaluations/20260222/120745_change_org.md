# OpenAIX Evaluation Report

**Target**: https://change.org
**Score**: 54/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T04:07:45Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 10
- snr_percent: 1.68
- raw_tokens: 115783
- clean_tokens: 1948

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 17
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1948
- estimated_cost_usd: 0.0584

### Permissions
- Score: 60
- allowed_agents: ['ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 135
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.change.org']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.