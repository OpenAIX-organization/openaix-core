# OpenAIX Evaluation Report

**Target**: https://cookiedatabase.org
**Score**: 54/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-13T11:19:08Z
**Site Type**: documentation (confidence: 33%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 27
- snr_percent: 4.52
- raw_tokens: 44200
- clean_tokens: 1996

### Semantic
- Score: 47
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 8
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1996
- estimated_cost_usd: 0.0599

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 667
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://cookiedatabase.org/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.