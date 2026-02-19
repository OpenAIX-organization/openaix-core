# OpenAIX Evaluation Report

**Target**: https://tumblr.com
**Score**: 39/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-19T13:09:24Z
**Site Type**: documentation (confidence: 0%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 2
- snr_percent: 0.39
- raw_tokens: 53122
- clean_tokens: 209

### Semantic
- Score: 29
- semantic_tags_used: ['nav', 'main', 'aside', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 209
- estimated_cost_usd: 0.0063

### Permissions
- Score: 60
- allowed_agents: ['GPTBot', 'ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 198
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://tumblr.com/graphql', 'https://tumblr.com/docs/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.