# OpenAIX Evaluation Report

**Target**: https://rapid7.com
**Score**: 50/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T19:01:24Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 4%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 25
- snr_percent: 4.08
- raw_tokens: 164191
- clean_tokens: 6705

### Semantic
- Score: 62
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 88
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6705
- estimated_cost_usd: 0.2011

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 870
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://rapid7.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.