# OpenAIX Evaluation Report

**Target**: https://proofpoint.com
**Score**: 46/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T13:15:30Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 14%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 58
- snr_percent: 13.96
- raw_tokens: 53867
- clean_tokens: 7521

### Semantic
- Score: 56
- semantic_tags_used: ['article', 'nav', 'main', 'section']
- json_ld_present: False
- hidden_gem: False
- images_total: 123
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 7521
- estimated_cost_usd: 0.2256

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 159
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.