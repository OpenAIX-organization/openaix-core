# OpenAIX Evaluation Report

**Target**: https://wireshark.org
**Score**: 46/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-15T21:08:11Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 26
- snr_percent: 4.38
- raw_tokens: 74377
- clean_tokens: 3255

### Semantic
- Score: 64
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 8
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3255
- estimated_cost_usd: 0.0976

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 97
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