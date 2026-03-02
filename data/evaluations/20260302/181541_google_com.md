# OpenAIX Evaluation Report

**Target**: https://google.com/workspace/security
**Score**: 63/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-03-02T10:15:41Z
**Site Type**: product (confidence: 50%)

---

## Metrics

- **snr**: 24%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 76
- snr_percent: 23.95
- raw_tokens: 212696
- clean_tokens: 50936

### Semantic
- Score: 78
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 214
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 50936
- estimated_cost_usd: 1.5281

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 25
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://google.com/workspace/security/graphql', 'https://google.com/workspace/security/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📝 Add /llms.txt to describe your site for AI agents.