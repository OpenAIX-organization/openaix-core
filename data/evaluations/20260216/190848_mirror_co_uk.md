# OpenAIX Evaluation Report

**Target**: https://mirror.co.uk
**Score**: 31/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-16T11:08:48Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 4%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 25
- snr_percent: 4.22
- raw_tokens: 330920
- clean_tokens: 13962

### Semantic
- Score: 36
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 1
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 13962
- estimated_cost_usd: 0.4189

### Permissions
- Score: 50
- allowed_agents: ['ChatGPT-User', 'Google-Extended']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 172
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.