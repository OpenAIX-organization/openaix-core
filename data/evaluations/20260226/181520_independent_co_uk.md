# OpenAIX Evaluation Report

**Target**: https://independent.co.uk/books
**Score**: 52/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T10:15:20Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 25
- snr_percent: 4.16
- raw_tokens: 68226
- clean_tokens: 2838

### Semantic
- Score: 51
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 4
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2838
- estimated_cost_usd: 0.0851

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 132
- http_status: 404

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.independent.co.uk']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.