# OpenAIX Evaluation Report

**Target**: https://localnews8.com
**Score**: 39/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T03:16:22Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 4%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 21
- snr_percent: 3.58
- raw_tokens: 194924
- clean_tokens: 6975

### Semantic
- Score: 52
- semantic_tags_used: ['article', 'nav', 'header', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 34
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6975
- estimated_cost_usd: 0.2092

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 8
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
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.