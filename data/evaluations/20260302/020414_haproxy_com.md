# OpenAIX Evaluation Report

**Target**: https://haproxy.com
**Score**: 58/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T18:04:14Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 6%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['graphql', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 34
- snr_percent: 6.01
- raw_tokens: 147282
- clean_tokens: 8846

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 34
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8846
- estimated_cost_usd: 0.2654

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 89
- http_status: 200

### Api Availability
- Score: 35
- features: ['graphql', 'cli_tool']
- endpoints_found: ['https://haproxy.com/graphql']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.