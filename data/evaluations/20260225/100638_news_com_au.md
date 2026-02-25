# OpenAIX Evaluation Report

**Target**: https://news.com.au
**Score**: 55/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T02:06:38Z
**Site Type**: product (confidence: 32%)

---

## Metrics

- **snr**: 17%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 64
- snr_percent: 17.04
- raw_tokens: 169541
- clean_tokens: 28896

### Semantic
- Score: 67
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 95
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 28896
- estimated_cost_usd: 0.8669

### Permissions
- Score: 50
- allowed_agents: ['GPTBot', 'ChatGPT-User']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 1065
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.news.com.au']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.