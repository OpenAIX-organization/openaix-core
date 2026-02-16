# OpenAIX Evaluation Report

**Target**: https://nymag.com
**Score**: 37/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-16T03:15:29Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 24
- snr_percent: 3.98
- raw_tokens: 473055
- clean_tokens: 18804

### Semantic
- Score: 74
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 46
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 18804
- estimated_cost_usd: 0.5641

### Permissions
- Score: 50
- allowed_agents: ['GPTBot', 'Google-Extended']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 11
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.