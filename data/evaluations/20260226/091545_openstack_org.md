# OpenAIX Evaluation Report

**Target**: https://openstack.org
**Score**: 52/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T01:15:45Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 19
- snr_percent: 3.15
- raw_tokens: 95527
- clean_tokens: 3007

### Semantic
- Score: 62
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 19
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3007
- estimated_cost_usd: 0.0902

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 39
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.openstack.org']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.