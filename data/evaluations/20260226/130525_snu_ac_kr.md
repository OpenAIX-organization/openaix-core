# OpenAIX Evaluation Report

**Target**: https://snu.ac.kr
**Score**: 54/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T05:05:25Z
**Site Type**: platform (confidence: 62%)

---

## Metrics

- **snr**: 44%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 100
- snr_percent: 43.64
- raw_tokens: 41716
- clean_tokens: 18203

### Semantic
- Score: 61
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 65
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 18203
- estimated_cost_usd: 0.5461

### Permissions
- Score: 70
- allowed_agents: ['anthropic-ai', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'ClaudeBot']
- llms_txt_present: False
- response_time_ms: 1384
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.snu.ac.kr']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.