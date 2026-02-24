# OpenAIX Evaluation Report

**Target**: https://goodreads.com
**Score**: 69/100
**Grade**: Class B (Human Optimized)
**Timestamp**: 2026-02-24T00:13:04Z
**Site Type**: documentation (confidence: 50%)

---

## Metrics

- **snr**: 37%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 96
- snr_percent: 37.12
- raw_tokens: 16761
- clean_tokens: 6222

### Semantic
- Score: 46
- semantic_tags_used: ['article', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 56
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6222
- estimated_cost_usd: 0.1867

### Permissions
- Score: 80
- allowed_agents: ['anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot']
- llms_txt_present: False
- response_time_ms: 294
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.goodreads.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.