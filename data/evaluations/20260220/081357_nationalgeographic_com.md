# OpenAIX Evaluation Report

**Target**: https://nationalgeographic.com
**Score**: 47/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-20T00:13:57Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 21
- snr_percent: 3.57
- raw_tokens: 179355
- clean_tokens: 6395

### Semantic
- Score: 56
- semantic_tags_used: ['article', 'header', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 3
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6395
- estimated_cost_usd: 0.1918

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 219
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.nationalgeographic.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.