# OpenAIX Evaluation Report

**Target**: https://weforum.org
**Score**: 49/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-24T12:15:24Z
**Site Type**: platform (confidence: 50%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 11
- snr_percent: 1.83
- raw_tokens: 255183
- clean_tokens: 4682

### Semantic
- Score: 58
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 28
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4682
- estimated_cost_usd: 0.1405

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 253
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.weforum.org']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.