# OpenAIX Evaluation Report

**Target**: https://finma.ch
**Score**: 56/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T11:16:57Z
**Site Type**: platform (confidence: 50%)

---

## Metrics

- **snr**: 43%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 100
- snr_percent: 42.61
- raw_tokens: 23248
- clean_tokens: 9905

### Semantic
- Score: 60
- semantic_tags_used: ['nav', 'header', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 24
- heading_levels: 3
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 9905
- estimated_cost_usd: 0.2971

### Permissions
- Score: 95
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 1665
- http_status: 200

### Api Availability
- Score: 20
- features: ['api_subdomain']
- endpoints_found: ['https://api.finma.ch']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.