# OpenAIX Evaluation Report

**Target**: https://play.google.com
**Score**: 34/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-21T00:11:38Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 1%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 5
- snr_percent: 0.86
- raw_tokens: 1084884
- clean_tokens: 9299

### Semantic
- Score: 39
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 122
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 9299
- estimated_cost_usd: 0.279

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 311
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