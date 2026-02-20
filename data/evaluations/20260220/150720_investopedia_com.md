# OpenAIX Evaluation Report

**Target**: https://investopedia.com
**Score**: 52/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-20T07:07:20Z
**Site Type**: product (confidence: 33%)

---

## Metrics

- **snr**: 4%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 26
- snr_percent: 4.36
- raw_tokens: 159259
- clean_tokens: 6943

### Semantic
- Score: 74
- semantic_tags_used: ['nav', 'header', 'main', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 28
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6943
- estimated_cost_usd: 0.2083

### Permissions
- Score: 50
- allowed_agents: ['GPTBot', 'ChatGPT-User']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 162
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.investopedia.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.