# OpenAIX Evaluation Report

**Target**: https://mediawiki.org
**Score**: 76/100
**Grade**: Class A (Agent Friendly)
**Timestamp**: 2026-02-15T03:08:48Z
**Site Type**: content (confidence: 41%)

---

## Metrics

- **snr**: 23%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 74
- snr_percent: 22.72
- raw_tokens: 23534
- clean_tokens: 5347

### Semantic
- Score: 85
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 17
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 5347
- estimated_cost_usd: 0.1604

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 49
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