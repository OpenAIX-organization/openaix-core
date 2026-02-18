# OpenAIX Evaluation Report

**Target**: https://www.ncbi.nlm.nih.gov
**Score**: 56/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T22:08:38Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 13%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 55
- snr_percent: 12.7
- raw_tokens: 10815
- clean_tokens: 1373

### Semantic
- Score: 48
- semantic_tags_used: ['nav', 'header', 'section']
- json_ld_present: False
- hidden_gem: False
- images_total: 10
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1373
- estimated_cost_usd: 0.0412

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 64
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.ncbi.nlm.nih.gov']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.