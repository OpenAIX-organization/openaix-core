# OpenAIX Evaluation Report

**Target**: https://nzherald.co.nz
**Score**: 38/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T03:03:00Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 18
- snr_percent: 2.98
- raw_tokens: 902215
- clean_tokens: 26845

### Semantic
- Score: 56
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 98
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 26845
- estimated_cost_usd: 0.8053

### Permissions
- Score: 90
- allowed_agents: ['GPTBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['CCBot']
- llms_txt_present: False
- response_time_ms: 432
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
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.