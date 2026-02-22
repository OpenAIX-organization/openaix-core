# OpenAIX Evaluation Report

**Target**: https://nodejs.org
**Score**: 52/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T04:06:36Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 0%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 2
- snr_percent: 0.36
- raw_tokens: 185156
- clean_tokens: 658

### Semantic
- Score: 44
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 1
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 658
- estimated_cost_usd: 0.0197

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 96
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.nodejs.org', 'https://nodejs.org/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.