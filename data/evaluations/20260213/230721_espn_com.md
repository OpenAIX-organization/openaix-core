# OpenAIX Evaluation Report

**Target**: https://espn.com
**Score**: 54/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-13T15:07:21Z
**Site Type**: product (confidence: 34%)

---

## Metrics

- **snr**: 14%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 57
- snr_percent: 13.72
- raw_tokens: 80459
- clean_tokens: 11038

### Semantic
- Score: 59
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 107
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 11038
- estimated_cost_usd: 0.3311

### Permissions
- Score: 50
- allowed_agents: ['ClaudeBot', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ChatGPT-User', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 84
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.espn.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📝 Add /llms.txt to describe your site for AI agents.