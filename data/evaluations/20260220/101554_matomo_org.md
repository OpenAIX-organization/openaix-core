# OpenAIX Evaluation Report

**Target**: https://matomo.org
**Score**: 64/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-20T02:15:54Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 11%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 51
- snr_percent: 10.6
- raw_tokens: 96969
- clean_tokens: 10282

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 62
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 10282
- estimated_cost_usd: 0.3085

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 6
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.matomo.org', 'https://matomo.org/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.