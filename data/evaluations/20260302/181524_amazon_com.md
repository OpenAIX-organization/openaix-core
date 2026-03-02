# OpenAIX Evaluation Report

**Target**: https://amazon.com/personalize
**Score**: 44/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T10:15:24Z
**Site Type**: product (confidence: 36%)

---

## Metrics

- **snr**: 5%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 28
- snr_percent: 4.7
- raw_tokens: 260655
- clean_tokens: 12249

### Semantic
- Score: 54
- semantic_tags_used: ['nav', 'header']
- json_ld_present: False
- hidden_gem: False
- images_total: 47
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 12249
- estimated_cost_usd: 0.3675

### Permissions
- Score: 40
- allowed_agents: ['anthropic-ai']
- blocked_agents: ['GPTBot', 'CCBot', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 791
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.amazon.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Class C - Needs Improvement. Bottom 50%.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.