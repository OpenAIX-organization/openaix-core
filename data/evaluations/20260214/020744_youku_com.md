# OpenAIX Evaluation Report

**Target**: https://youku.com
**Score**: 38/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-13T18:07:44Z
**Site Type**: documentation (confidence: 0%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 3

---

## Dimensions


### Snr
- Score: 27
- snr_percent: 4.51
- raw_tokens: 415494
- clean_tokens: 18741

### Semantic
- Score: 15
- semantic_tags_used: []
- json_ld_present: False
- hidden_gem: False
- images_total: 175
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 18741
- estimated_cost_usd: 0.5622

### Permissions
- Score: 95
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 1614
- http_status: 200

### Api Availability
- Score: 70
- features: ['graphql', 'api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://youku.com/graphql', 'https://api.youku.com', 'https://youku.com/api']
- has_api: True
- has_comprehensive_api: True

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.