# OpenAIX Evaluation Report

**Target**: https://news.google.com
**Score**: 51/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-15T12:06:46Z
**Site Type**: platform (confidence: 54%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 3
- snr_percent: 0.46
- raw_tokens: 754028
- clean_tokens: 3481

### Semantic
- Score: 51
- semantic_tags_used: ['header', 'main', 'section']
- json_ld_present: True
- hidden_gem: False
- images_total: 11
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3481
- estimated_cost_usd: 0.1044

### Permissions
- Score: 80
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: True
- response_time_ms: 394
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://news.google.com/graphql', 'https://news.google.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.