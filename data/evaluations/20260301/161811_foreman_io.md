# OpenAIX Evaluation Report

**Target**: https://foreman.io
**Score**: 68/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T08:18:11Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 27
- snr_percent: 4.51
- raw_tokens: 40848
- clean_tokens: 1842

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 4
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1842
- estimated_cost_usd: 0.0553

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 21
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://foreman.io/graphql', 'https://foreman.io/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.