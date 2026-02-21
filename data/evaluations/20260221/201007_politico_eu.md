# OpenAIX Evaluation Report

**Target**: https://politico.eu
**Score**: 51/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-21T12:10:07Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 8%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 42
- snr_percent: 7.9
- raw_tokens: 134854
- clean_tokens: 10647

### Semantic
- Score: 71
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 44
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 10647
- estimated_cost_usd: 0.3194

### Permissions
- Score: 30
- allowed_agents: []
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 50
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.politico.eu']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📝 Add /llms.txt to describe your site for AI agents.