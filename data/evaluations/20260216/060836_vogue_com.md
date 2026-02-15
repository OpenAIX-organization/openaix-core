# OpenAIX Evaluation Report

**Target**: https://vogue.com
**Score**: 46/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-15T22:08:36Z
**Site Type**: documentation (confidence: 26%)

---

## Metrics

- **snr**: 2%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 10
- snr_percent: 1.65
- raw_tokens: 534690
- clean_tokens: 8836

### Semantic
- Score: 81
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 74
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8836
- estimated_cost_usd: 0.2651

### Permissions
- Score: 60
- allowed_agents: ['GPTBot', 'anthropic-ai', 'ChatGPT-User']
- blocked_agents: ['CCBot', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 72
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.vogue.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.