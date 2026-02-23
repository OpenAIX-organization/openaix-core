# OpenAIX Evaluation Report

**Target**: https://wordpress.org
**Score**: 62/100
**Grade**: Class A (Agent Friendly)
**Timestamp**: 2026-02-23T02:11:31Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 21
- snr_percent: 3.49
- raw_tokens: 55569
- clean_tokens: 1939

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 17
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1939
- estimated_cost_usd: 0.0582

### Permissions
- Score: 100
- allowed_agents: []
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 84
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.wordpress.org']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.