# OpenAIX Evaluation Report

**Target**: https://myfitnesspal.com
**Score**: 52/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-02T06:12:34Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 11
- snr_percent: 1.81
- raw_tokens: 232646
- clean_tokens: 4221

### Semantic
- Score: 53
- semantic_tags_used: ['section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 52
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 4221
- estimated_cost_usd: 0.1266

### Permissions
- Score: 90
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['ChatGPT-User']
- llms_txt_present: False
- response_time_ms: 501
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.myfitnesspal.com', 'https://myfitnesspal.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.