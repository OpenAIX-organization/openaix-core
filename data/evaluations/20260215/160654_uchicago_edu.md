# OpenAIX Evaluation Report

**Target**: https://uchicago.edu
**Score**: 53/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-15T08:06:54Z
**Site Type**: platform (confidence: 63%)

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
- Score: 18
- snr_percent: 2.97
- raw_tokens: 43546
- clean_tokens: 1294

### Semantic
- Score: 61
- semantic_tags_used: ['main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 3
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1294
- estimated_cost_usd: 0.0388

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 432
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.uchicago.edu']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.