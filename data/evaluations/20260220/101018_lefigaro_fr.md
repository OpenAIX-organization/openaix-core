# OpenAIX Evaluation Report

**Target**: https://lefigaro.fr
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-20T02:10:18Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 13%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 57
- snr_percent: 13.37
- raw_tokens: 314488
- clean_tokens: 42052

### Semantic
- Score: 81
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 269
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 42052
- estimated_cost_usd: 1.2616

### Permissions
- Score: 40
- allowed_agents: ['PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 34
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://lefigaro.fr/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.