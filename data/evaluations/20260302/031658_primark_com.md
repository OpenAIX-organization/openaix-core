# OpenAIX Evaluation Report

**Target**: https://primark.com
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T19:16:58Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 21
- snr_percent: 3.47
- raw_tokens: 362578
- clean_tokens: 12582

### Semantic
- Score: 64
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 17
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 12582
- estimated_cost_usd: 0.3775

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 70
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://primark.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.