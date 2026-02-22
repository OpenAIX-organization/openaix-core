# OpenAIX Evaluation Report

**Target**: https://aljazeera.com
**Score**: 52/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T04:09:38Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 10
- snr_percent: 1.74
- raw_tokens: 257198
- clean_tokens: 4477

### Semantic
- Score: 90
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 18
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4477
- estimated_cost_usd: 0.1343

### Permissions
- Score: 50
- allowed_agents: ['CCBot', 'Google-Extended']
- blocked_agents: ['GPTBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 223
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.aljazeera.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.