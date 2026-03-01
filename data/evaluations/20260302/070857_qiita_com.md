# OpenAIX Evaluation Report

**Target**: https://qiita.com
**Score**: 54/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T23:08:57Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 12%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 55
- snr_percent: 12.43
- raw_tokens: 123365
- clean_tokens: 15339

### Semantic
- Score: 55
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 64
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 15339
- estimated_cost_usd: 0.4602

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 890
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.qiita.com', 'https://qiita.com/docs/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.