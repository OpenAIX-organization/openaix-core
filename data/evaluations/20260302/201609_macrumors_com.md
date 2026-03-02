# OpenAIX Evaluation Report

**Target**: https://macrumors.com
**Score**: 70/100
**Grade**: Class A (Agent Friendly)
**Timestamp**: 2026-03-02T12:16:09Z
**Site Type**: product (confidence: 32%)

---

## Metrics

- **snr**: 29%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 84
- snr_percent: 29.06
- raw_tokens: 151006
- clean_tokens: 43882

### Semantic
- Score: 81
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 221
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 43882
- estimated_cost_usd: 1.3165

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 42
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.macrumors.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📝 Add /llms.txt to describe your site for AI agents.