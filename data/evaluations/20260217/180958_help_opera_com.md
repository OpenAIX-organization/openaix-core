# OpenAIX Evaluation Report

**Target**: https://help.opera.com
**Score**: 76/100
**Grade**: Class A (Agent Friendly)
**Timestamp**: 2026-02-17T10:09:58Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 20%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 71
- snr_percent: 20.42
- raw_tokens: 15032
- clean_tokens: 3070

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 9
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3070
- estimated_cost_usd: 0.0921

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 289
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://help.opera.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Agent Friendly. Good structure and API access.
- 📝 Add /llms.txt to describe your site for AI agents.