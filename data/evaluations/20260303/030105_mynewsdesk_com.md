# OpenAIX Evaluation Report

**Target**: https://mynewsdesk.com
**Score**: 64/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T19:01:05Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['graphql', 'api_subdomain', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 28
- snr_percent: 4.74
- raw_tokens: 78326
- clean_tokens: 3710

### Semantic
- Score: 71
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 23
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3710
- estimated_cost_usd: 0.1113

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 946
- http_status: 200

### Api Availability
- Score: 55
- features: ['graphql', 'api_subdomain', 'cli_tool']
- endpoints_found: ['https://mynewsdesk.com/graphql', 'https://api.mynewsdesk.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.