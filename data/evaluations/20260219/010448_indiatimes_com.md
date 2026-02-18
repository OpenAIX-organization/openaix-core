# OpenAIX Evaluation Report

**Target**: https://indiatimes.com
**Score**: 55/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T17:04:48Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 13%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 56
- snr_percent: 12.88
- raw_tokens: 48746
- clean_tokens: 6279

### Semantic
- Score: 64
- semantic_tags_used: ['article', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 70
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6279
- estimated_cost_usd: 0.1884

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 14
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.indiatimes.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.