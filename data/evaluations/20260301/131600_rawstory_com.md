# OpenAIX Evaluation Report

**Target**: https://rawstory.com
**Score**: 47/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T05:16:00Z
**Site Type**: platform (confidence: 41%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 24
- snr_percent: 3.98
- raw_tokens: 144638
- clean_tokens: 5759

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav']
- json_ld_present: True
- hidden_gem: True
- images_total: 7
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 5759
- estimated_cost_usd: 0.1728

### Permissions
- Score: 60
- allowed_agents: ['anthropic-ai', 'ClaudeBot', 'ChatGPT-User']
- blocked_agents: ['GPTBot', 'CCBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 92
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.