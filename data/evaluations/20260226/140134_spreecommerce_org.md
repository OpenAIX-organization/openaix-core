# OpenAIX Evaluation Report

**Target**: https://spreecommerce.org
**Score**: 59/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T06:01:34Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 12%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 55
- snr_percent: 12.41
- raw_tokens: 54692
- clean_tokens: 6786

### Semantic
- Score: 62
- semantic_tags_used: ['article', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 129
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6786
- estimated_cost_usd: 0.2036

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 97
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.spreecommerce.org', 'https://spreecommerce.org/reference/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.