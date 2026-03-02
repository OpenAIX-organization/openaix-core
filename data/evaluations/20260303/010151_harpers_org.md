# OpenAIX Evaluation Report

**Target**: https://harpers.org
**Score**: 62/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T17:01:51Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 23%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 74
- snr_percent: 22.64
- raw_tokens: 34452
- clean_tokens: 7801

### Semantic
- Score: 60
- semantic_tags_used: ['nav', 'header', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 36
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 7801
- estimated_cost_usd: 0.234

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
- endpoints_found: ['https://api.harpers.org', 'https://harpers.org/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.