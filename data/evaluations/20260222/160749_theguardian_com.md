# OpenAIX Evaluation Report

**Target**: https://theguardian.com
**Score**: 34/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T08:07:49Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 5%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 29
- snr_percent: 4.86
- raw_tokens: 438814
- clean_tokens: 21305

### Semantic
- Score: 56
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 136
- heading_levels: 3
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 21305
- estimated_cost_usd: 0.6391

### Permissions
- Score: 60
- allowed_agents: ['GPTBot', 'ChatGPT-User', 'Google-Extended']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 124
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