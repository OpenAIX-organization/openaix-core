# OpenAIX Evaluation Report

**Target**: https://solarwinds.com
**Score**: 45/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T19:16:08Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 2%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 10
- snr_percent: 1.62
- raw_tokens: 506389
- clean_tokens: 8213

### Semantic
- Score: 67
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 42
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 8213
- estimated_cost_usd: 0.2464

### Permissions
- Score: 85
- allowed_agents: ['GPTBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['CCBot']
- llms_txt_present: False
- response_time_ms: 1626
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.solarwinds.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.