# OpenAIX Evaluation Report

**Target**: https://merriam-webster.com
**Score**: 51/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T20:09:32Z
**Site Type**: platform (confidence: 54%)

---

## Metrics

- **snr**: 7%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 38
- snr_percent: 6.89
- raw_tokens: 88300
- clean_tokens: 6085

### Semantic
- Score: 60
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 25
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6085
- estimated_cost_usd: 0.1825

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 11
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.merriam-webster.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.