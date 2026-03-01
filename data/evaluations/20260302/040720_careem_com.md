# OpenAIX Evaluation Report

**Target**: https://careem.com
**Score**: 56/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-03-01T20:07:20Z
**Site Type**: content (confidence: 58%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 17
- snr_percent: 2.87
- raw_tokens: 140532
- clean_tokens: 4040

### Semantic
- Score: 67
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 70
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4040
- estimated_cost_usd: 0.1212

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 163
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.careem.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.