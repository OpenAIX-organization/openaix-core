# OpenAIX Evaluation Report

**Target**: https://jquery.com
**Score**: 65/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-22T04:08:02Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 22%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 73
- snr_percent: 22.09
- raw_tokens: 7805
- clean_tokens: 1724

### Semantic
- Score: 53
- semantic_tags_used: ['nav', 'header', 'section', 'aside', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 3
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1724
- estimated_cost_usd: 0.0517

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 11
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.jquery.com', 'https://jquery.com/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.