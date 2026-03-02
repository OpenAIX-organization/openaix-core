# OpenAIX Evaluation Report

**Target**: https://etymonline.com
**Score**: 55/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-03-02T13:16:04Z
**Site Type**: content (confidence: 100%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 20
- snr_percent: 3.4
- raw_tokens: 42295
- clean_tokens: 1440

### Semantic
- Score: 68
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 4
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1440
- estimated_cost_usd: 0.0432

### Permissions
- Score: 60
- allowed_agents: ['anthropic-ai', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'ClaudeBot', 'ChatGPT-User']
- llms_txt_present: False
- response_time_ms: 77
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.