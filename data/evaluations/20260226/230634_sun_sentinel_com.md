# OpenAIX Evaluation Report

**Target**: https://sun-sentinel.com
**Score**: 54/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T15:06:34Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 23%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 74
- snr_percent: 22.77
- raw_tokens: 75901
- clean_tokens: 17284

### Semantic
- Score: 67
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 42
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 17284
- estimated_cost_usd: 0.5185

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 7
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://sun-sentinel.com/graphql', 'https://sun-sentinel.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📝 Add /llms.txt to describe your site for AI agents.