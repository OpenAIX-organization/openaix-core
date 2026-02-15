# OpenAIX Evaluation Report

**Target**: https://openstreetmap.org
**Score**: 57/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-13T18:11:43Z
**Site Type**: content (confidence: 100%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 21
- snr_percent: 3.43
- raw_tokens: 10767
- clean_tokens: 369

### Semantic
- Score: 52
- semantic_tags_used: ['nav', 'header']
- json_ld_present: False
- hidden_gem: False
- images_total: 2
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 369
- estimated_cost_usd: 0.0111

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 360
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.openstreetmap.org']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.