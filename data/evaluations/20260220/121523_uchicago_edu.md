# OpenAIX Evaluation Report

**Target**: https://uchicago.edu
**Score**: 59/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-20T04:15:23Z
**Site Type**: content (confidence: 58%)

---

## Metrics

- **snr**: 3%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 18
- snr_percent: 2.94
- raw_tokens: 43505
- clean_tokens: 1278

### Semantic
- Score: 61
- semantic_tags_used: ['main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 3
- heading_levels: 2
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1278
- estimated_cost_usd: 0.0383

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 455
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.uchicago.edu']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.