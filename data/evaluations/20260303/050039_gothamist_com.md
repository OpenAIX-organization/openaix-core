# OpenAIX Evaluation Report

**Target**: https://gothamist.com
**Score**: 28/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T21:00:39Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 9
- snr_percent: 1.49
- raw_tokens: 251081
- clean_tokens: 3736

### Semantic
- Score: 19
- semantic_tags_used: ['header', 'main', 'section']
- json_ld_present: False
- hidden_gem: False
- images_total: 23
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3736
- estimated_cost_usd: 0.1121

### Permissions
- Score: 60
- allowed_agents: ['anthropic-ai', 'ClaudeBot', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'ChatGPT-User', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 60
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