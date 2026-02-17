# OpenAIX Evaluation Report

**Target**: https://matterport.com
**Score**: 65/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-17T12:15:52Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['openapi_spec', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 6
- snr_percent: 1.07
- raw_tokens: 113683
- clean_tokens: 1214

### Semantic
- Score: 53
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside']
- json_ld_present: False
- hidden_gem: False
- images_total: 25
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1214
- estimated_cost_usd: 0.0364

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 25
- http_status: 200

### Api Availability
- Score: 75
- features: ['openapi_spec', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://matterport.com/swagger.json', 'https://api.matterport.com', 'https://matterport.com/developers']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.