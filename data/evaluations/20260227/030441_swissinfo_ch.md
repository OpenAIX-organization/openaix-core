# OpenAIX Evaluation Report

**Target**: https://swissinfo.ch
**Score**: 45/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T19:04:41Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 12
- snr_percent: 2.08
- raw_tokens: 1117032
- clean_tokens: 23199

### Semantic
- Score: 74
- semantic_tags_used: ['article', 'nav', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 127
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 23199
- estimated_cost_usd: 0.696

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 385
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://swissinfo.ch/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.