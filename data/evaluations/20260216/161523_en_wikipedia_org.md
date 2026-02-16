# OpenAIX Evaluation Report

**Target**: https://en.wikipedia.org
**Score**: 71/100
**Grade**: Class A (Agent Friendly)
**Timestamp**: 2026-02-16T08:15:23Z
**Site Type**: content (confidence: 41%)

---

## Metrics

- **snr**: 37%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 95
- snr_percent: 36.8
- raw_tokens: 74984
- clean_tokens: 27597

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 25
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 27597
- estimated_cost_usd: 0.8279

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 29
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- ✅ Agent Friendly. Good structure and API access.
- 📝 Add /llms.txt to describe your site for AI agents.