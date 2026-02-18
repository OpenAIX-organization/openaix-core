# OpenAIX Evaluation Report

**Target**: https://espn.com
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T11:08:36Z
**Site Type**: platform (confidence: 41%)

---

## Metrics

- **snr**: 11%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 53
- snr_percent: 11.34
- raw_tokens: 81888
- clean_tokens: 9283

### Semantic
- Score: 59
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 98
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 9283
- estimated_cost_usd: 0.2785

### Permissions
- Score: 50
- allowed_agents: ['ClaudeBot', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ChatGPT-User', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 139
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.espn.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.