# OpenAIX Evaluation Report

**Target**: https://lefigaro.fr
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T17:06:07Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 14%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 57
- snr_percent: 13.54
- raw_tokens: 336286
- clean_tokens: 45543

### Semantic
- Score: 81
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 299
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 45543
- estimated_cost_usd: 1.3663

### Permissions
- Score: 40
- allowed_agents: ['PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 41
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://lefigaro.fr/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.