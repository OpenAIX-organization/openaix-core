# OpenAIX Evaluation Report

**Target**: https://biblegateway.com
**Score**: 70/100
**Grade**: Class A (Agent Friendly)
**Timestamp**: 2026-03-03T03:02:15Z
**Site Type**: documentation (confidence: 33%)

---

## Metrics

- **snr**: 17%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 63
- snr_percent: 16.64
- raw_tokens: 34550
- clean_tokens: 5749

### Semantic
- Score: 64
- semantic_tags_used: ['article', 'nav', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 7
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 5749
- estimated_cost_usd: 0.1725

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 9
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://biblegateway.com/graphql', 'https://biblegateway.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.