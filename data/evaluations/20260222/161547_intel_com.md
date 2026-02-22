# OpenAIX Evaluation Report

**Target**: https://intel.com
**Score**: 62/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T08:15:47Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 10%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 49
- snr_percent: 9.8
- raw_tokens: 34790
- clean_tokens: 3411

### Semantic
- Score: 66
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 5
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3411
- estimated_cost_usd: 0.1023

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 163
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.intel.com', 'https://intel.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.