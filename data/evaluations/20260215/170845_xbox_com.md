# OpenAIX Evaluation Report

**Target**: https://xbox.com
**Score**: 47/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-15T09:08:45Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 21
- snr_percent: 3.47
- raw_tokens: 173185
- clean_tokens: 6014

### Semantic
- Score: 60
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 48
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6014
- estimated_cost_usd: 0.1804

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 127
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://xbox.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.