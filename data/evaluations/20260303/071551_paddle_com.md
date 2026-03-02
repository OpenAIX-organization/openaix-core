# OpenAIX Evaluation Report

**Target**: https://paddle.com
**Score**: 40/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T23:15:51Z
**Site Type**: platform (confidence: 36%)

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
- Score: 16
- snr_percent: 2.63
- raw_tokens: 246688
- clean_tokens: 6490

### Semantic
- Score: 59
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 51
- heading_levels: 6
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6490
- estimated_cost_usd: 0.1947

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 37
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
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.