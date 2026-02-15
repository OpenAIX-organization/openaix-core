# OpenAIX Evaluation Report

**Target**: https://thedailybeast.com
**Score**: 36/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T14:07:07Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 18
- snr_percent: 3.05
- raw_tokens: 344529
- clean_tokens: 10515

### Semantic
- Score: 39
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 63
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 10515
- estimated_cost_usd: 0.3155

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 169
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
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.