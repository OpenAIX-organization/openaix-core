# OpenAIX Evaluation Report

**Target**: https://bitly.com
**Score**: 62/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-18T20:10:32Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 15%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['graphql', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 60
- snr_percent: 14.96
- raw_tokens: 48339
- clean_tokens: 7230

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 77
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 7230
- estimated_cost_usd: 0.2169

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 92
- http_status: 200

### Api Availability
- Score: 35
- features: ['graphql', 'cli_tool']
- endpoints_found: ['https://bitly.com/graphql']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.