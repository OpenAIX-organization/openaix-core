# OpenAIX Evaluation Report

**Target**: https://nypost.com
**Score**: 44/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T15:11:46Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 6%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 34
- snr_percent: 6.08
- raw_tokens: 460817
- clean_tokens: 28007

### Semantic
- Score: 74
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 126
- heading_levels: 4
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 28007
- estimated_cost_usd: 0.8402

### Permissions
- Score: 40
- allowed_agents: ['GPTBot', 'ChatGPT-User']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 3229
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.nypost.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.