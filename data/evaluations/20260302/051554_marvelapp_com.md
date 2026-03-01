# OpenAIX Evaluation Report

**Target**: https://marvelapp.com
**Score**: 71/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T21:15:54Z
**Site Type**: platform (confidence: 33%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Low
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 4
- snr_percent: 0.6
- raw_tokens: 231051
- clean_tokens: 1397

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 4
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1397
- estimated_cost_usd: 0.0419

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 6
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://marvelapp.com/graphql', 'https://api.marvelapp.com', 'https://marvelapp.com/developers']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.