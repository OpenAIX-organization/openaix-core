# OpenAIX Evaluation Report

**Target**: https://leparisien.fr
**Score**: 43/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-27T01:15:41Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Very High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 22
- snr_percent: 3.58
- raw_tokens: 1505071
- clean_tokens: 53933

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 260
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 53933
- estimated_cost_usd: 1.618

### Permissions
- Score: 50
- allowed_agents: ['ChatGPT-User', 'Google-Extended']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 412
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.