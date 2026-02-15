# OpenAIX Evaluation Report

**Target**: https://thetimes.co.uk
**Score**: 49/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T20:13:27Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 10%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 51
- snr_percent: 10.32
- raw_tokens: 566547
- clean_tokens: 58452

### Semantic
- Score: 86
- semantic_tags_used: ['nav', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 372
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 58452
- estimated_cost_usd: 1.7536

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 839
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.thetimes.co.uk']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.