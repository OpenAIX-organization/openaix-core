# OpenAIX Evaluation Report

**Target**: https://about.me
**Score**: 58/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T03:07:07Z
**Site Type**: product (confidence: 50%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 15
- snr_percent: 2.44
- raw_tokens: 33124
- clean_tokens: 808

### Semantic
- Score: 64
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 1
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 808
- estimated_cost_usd: 0.0242

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 100
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.about.me', 'https://about.me/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.