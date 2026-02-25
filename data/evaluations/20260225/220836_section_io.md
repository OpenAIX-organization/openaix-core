# OpenAIX Evaluation Report

**Target**: https://section.io
**Score**: 66/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T14:08:36Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 29
- snr_percent: 4.76
- raw_tokens: 78900
- clean_tokens: 3759

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 58
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3759
- estimated_cost_usd: 0.1128

### Permissions
- Score: 100
- allowed_agents: []
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 369
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://section.io/graphql', 'https://section.io/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.