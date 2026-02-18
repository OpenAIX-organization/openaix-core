# OpenAIX Evaluation Report

**Target**: https://redhat.com
**Score**: 46/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T14:15:36Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 2%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 15
- snr_percent: 2.44
- raw_tokens: 378503
- clean_tokens: 9219

### Semantic
- Score: 61
- semantic_tags_used: ['article', 'header', 'section']
- json_ld_present: False
- hidden_gem: False
- images_total: 48
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 9219
- estimated_cost_usd: 0.2766

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 81
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://redhat.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.