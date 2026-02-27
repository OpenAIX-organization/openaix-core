# OpenAIX Evaluation Report

**Target**: https://iheartradio.com
**Score**: 40/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-27T00:17:45Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 5%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 29
- snr_percent: 4.82
- raw_tokens: 236799
- clean_tokens: 11420

### Semantic
- Score: 49
- semantic_tags_used: ['article', 'nav', 'main', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 68
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 11420
- estimated_cost_usd: 0.3426

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 431
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
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.