# OpenAIX Evaluation Report

**Target**: https://realm.io
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T05:07:20Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 18
- snr_percent: 3.02
- raw_tokens: 137442
- clean_tokens: 4145

### Semantic
- Score: 57
- semantic_tags_used: ['nav', 'header', 'main', 'section']
- json_ld_present: True
- hidden_gem: False
- images_total: 32
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4145
- estimated_cost_usd: 0.1243

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 188
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://realm.io/docs/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.