# OpenAIX Evaluation Report

**Target**: https://freelancer.com
**Score**: 50/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T08:06:22Z
**Site Type**: platform (confidence: 41%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 17
- snr_percent: 2.77
- raw_tokens: 317040
- clean_tokens: 8784

### Semantic
- Score: 47
- semantic_tags_used: []
- json_ld_present: True
- hidden_gem: False
- images_total: 86
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8784
- estimated_cost_usd: 0.2635

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 73
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.freelancer.com', 'https://freelancer.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.