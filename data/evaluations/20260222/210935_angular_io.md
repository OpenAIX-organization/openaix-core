# OpenAIX Evaluation Report

**Target**: https://angular.io
**Score**: 59/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T13:09:35Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 18
- snr_percent: 2.93
- raw_tokens: 31628
- clean_tokens: 928

### Semantic
- Score: 54
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 928
- estimated_cost_usd: 0.0278

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 94
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://angular.io/graphql', 'https://angular.io/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.