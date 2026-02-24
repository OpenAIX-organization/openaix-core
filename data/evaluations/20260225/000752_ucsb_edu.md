# OpenAIX Evaluation Report

**Target**: https://ucsb.edu
**Score**: 54/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-24T16:07:52Z
**Site Type**: content (confidence: 58%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 9
- snr_percent: 1.48
- raw_tokens: 163637
- clean_tokens: 2429

### Semantic
- Score: 68
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2429
- estimated_cost_usd: 0.0729

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 198
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.ucsb.edu']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.