# OpenAIX Evaluation Report

**Target**: https://kubernetes.io
**Score**: 58/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-28T21:15:28Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 12%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 53
- snr_percent: 11.53
- raw_tokens: 15610
- clean_tokens: 1800

### Semantic
- Score: 66
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 10
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1800
- estimated_cost_usd: 0.054

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 14
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://kubernetes.io/docs/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.