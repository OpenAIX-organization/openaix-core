# OpenAIX Evaluation Report

**Target**: https://tumblr.com
**Score**: 38/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T08:07:29Z
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
- Score: 0
- snr_percent: 0.07
- raw_tokens: 48710
- clean_tokens: 36

### Semantic
- Score: 26
- semantic_tags_used: ['header', 'main', 'aside']
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 36
- estimated_cost_usd: 0.0011

### Permissions
- Score: 60
- allowed_agents: ['GPTBot', 'ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 69
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