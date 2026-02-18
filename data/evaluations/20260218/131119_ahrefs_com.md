# OpenAIX Evaluation Report

**Target**: https://ahrefs.com
**Score**: 55/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T05:11:19Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 13
- snr_percent: 2.15
- raw_tokens: 210632
- clean_tokens: 4532

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 60
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4532
- estimated_cost_usd: 0.136

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 52
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://ahrefs.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.