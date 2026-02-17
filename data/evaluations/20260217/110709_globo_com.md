# OpenAIX Evaluation Report

**Target**: https://globo.com
**Score**: 34/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T03:07:09Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 15
- snr_percent: 2.51
- raw_tokens: 823326
- clean_tokens: 20662

### Semantic
- Score: 60
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 56
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 20662
- estimated_cost_usd: 0.6199

### Permissions
- Score: 70
- allowed_agents: ['anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 708
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