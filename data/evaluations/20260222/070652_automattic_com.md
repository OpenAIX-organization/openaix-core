# OpenAIX Evaluation Report

**Target**: https://automattic.com
**Score**: 64/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-21T23:06:52Z
**Site Type**: documentation (confidence: 26%)

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
- raw_tokens: 35947
- clean_tokens: 1412

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 4
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1412
- estimated_cost_usd: 0.0424

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 4
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.automattic.com', 'https://automattic.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.