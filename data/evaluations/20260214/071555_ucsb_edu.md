# OpenAIX Evaluation Report

**Target**: https://ucsb.edu
**Score**: 54/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-13T23:15:55Z
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
- snr_percent: 1.49
- raw_tokens: 163645
- clean_tokens: 2436

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
- clean_tokens: 2436
- estimated_cost_usd: 0.0731

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 225
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.ucsb.edu']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.