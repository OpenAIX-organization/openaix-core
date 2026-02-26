# OpenAIX Evaluation Report

**Target**: https://openlibrary.org
**Score**: 52/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T10:05:23Z
**Site Type**: platform (confidence: 46%)

---

## Metrics

- **snr**: 28%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 82
- snr_percent: 28.3
- raw_tokens: 23196
- clean_tokens: 6565

### Semantic
- Score: 45
- semantic_tags_used: ['header', 'main', 'aside', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 74
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6565
- estimated_cost_usd: 0.197

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 33
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://openlibrary.org/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.