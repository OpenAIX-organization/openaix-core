# OpenAIX Evaluation Report

**Target**: https://espn.com
**Score**: 54/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-23T14:09:14Z
**Site Type**: product (confidence: 45%)

---

## Metrics

- **snr**: 13%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 57
- snr_percent: 13.39
- raw_tokens: 76059
- clean_tokens: 10188

### Semantic
- Score: 59
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 100
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 10188
- estimated_cost_usd: 0.3056

### Permissions
- Score: 50
- allowed_agents: ['ClaudeBot', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ChatGPT-User', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 86
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.espn.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.