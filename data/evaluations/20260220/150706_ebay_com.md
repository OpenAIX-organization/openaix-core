# OpenAIX Evaluation Report

**Target**: https://ebay.com
**Score**: 36/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-20T07:07:06Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 8%
- **token_cost**: Very High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 44
- snr_percent: 8.38
- raw_tokens: 234125
- clean_tokens: 19623

### Semantic
- Score: 56
- semantic_tags_used: ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 80
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 40
- cost_rating: Very High
- clean_tokens: 19623
- estimated_cost_usd: 0.5887

### Permissions
- Score: 60
- allowed_agents: ['GPTBot', 'ChatGPT-User', 'Google-Extended']
- blocked_agents: ['CCBot', 'anthropic-ai', 'ClaudeBot', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 586
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
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.