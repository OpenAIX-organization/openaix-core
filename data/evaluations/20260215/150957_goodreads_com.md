# OpenAIX Evaluation Report

**Target**: https://goodreads.com
**Score**: 70/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-15T07:09:57Z
**Site Type**: documentation (confidence: 50%)

---

## Metrics

- **snr**: 39%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 98
- snr_percent: 38.82
- raw_tokens: 15918
- clean_tokens: 6180

### Semantic
- Score: 46
- semantic_tags_used: ['article', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 56
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6180
- estimated_cost_usd: 0.1854

### Permissions
- Score: 80
- allowed_agents: ['anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot']
- llms_txt_present: False
- response_time_ms: 298
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.goodreads.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Agent Friendly. Good structure and API access.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.