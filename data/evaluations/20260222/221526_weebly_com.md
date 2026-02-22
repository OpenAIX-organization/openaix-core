# OpenAIX Evaluation Report

**Target**: https://weebly.com
**Score**: 68/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-22T14:15:26Z
**Site Type**: product (confidence: 32%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 24
- snr_percent: 3.93
- raw_tokens: 42486
- clean_tokens: 1669

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 13
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1669
- estimated_cost_usd: 0.0501

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 116
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.weebly.com', 'https://weebly.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.