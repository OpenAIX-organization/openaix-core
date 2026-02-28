# OpenAIX Evaluation Report

**Target**: https://medpagetoday.com
**Score**: 63/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-28T07:05:54Z
**Site Type**: product (confidence: 32%)

---

## Metrics

- **snr**: 15%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 61
- snr_percent: 15.37
- raw_tokens: 52680
- clean_tokens: 8097

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 45
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8097
- estimated_cost_usd: 0.2429

### Permissions
- Score: 40
- allowed_agents: ['Google-Extended']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 195
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.medpagetoday.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📝 Add /llms.txt to describe your site for AI agents.