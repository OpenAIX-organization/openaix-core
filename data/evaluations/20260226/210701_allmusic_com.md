# OpenAIX Evaluation Report

**Target**: https://allmusic.com
**Score**: 68/100
**Grade**: Class A (Agent Friendly)
**Timestamp**: 2026-02-26T13:07:01Z
**Site Type**: content (confidence: 100%)

---

## Metrics

- **snr**: 23%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 75
- snr_percent: 23.02
- raw_tokens: 28993
- clean_tokens: 6673

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 37
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6673
- estimated_cost_usd: 0.2002

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 106
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://allmusic.com/graphql', 'https://allmusic.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📝 Add /llms.txt to describe your site for AI agents.