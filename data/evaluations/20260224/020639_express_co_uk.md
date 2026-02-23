# OpenAIX Evaluation Report

**Target**: https://express.co.uk
**Score**: 40/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-23T18:06:39Z
**Site Type**: platform (confidence: 41%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 28
- snr_percent: 4.7
- raw_tokens: 422112
- clean_tokens: 19824

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 164
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 19824
- estimated_cost_usd: 0.5947

### Permissions
- Score: 50
- allowed_agents: ['ChatGPT-User', 'Google-Extended']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 20
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