# OpenAIX Evaluation Report

**Target**: https://nintendo.com
**Score**: 46/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T03:16:16Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 2%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 14
- snr_percent: 2.26
- raw_tokens: 614980
- clean_tokens: 13882

### Semantic
- Score: 85
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: True
- hidden_gem: True
- images_total: 143
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 13882
- estimated_cost_usd: 0.4165

### Permissions
- Score: 60
- allowed_agents: ['anthropic-ai', 'ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'ClaudeBot', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 135
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.