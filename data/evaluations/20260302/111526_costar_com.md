# OpenAIX Evaluation Report

**Target**: https://costar.com
**Score**: 43/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T03:15:26Z
**Site Type**: product (confidence: 33%)

---

## Metrics

- **snr**: 3%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 17
- snr_percent: 2.9
- raw_tokens: 475189
- clean_tokens: 13766

### Semantic
- Score: 42
- semantic_tags_used: ['nav', 'header', 'section']
- json_ld_present: False
- hidden_gem: False
- images_total: 36
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 13766
- estimated_cost_usd: 0.413

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 74
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.costar.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.