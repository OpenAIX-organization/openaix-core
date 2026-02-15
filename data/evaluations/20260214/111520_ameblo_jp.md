# OpenAIX Evaluation Report

**Target**: https://ameblo.jp
**Score**: 63/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-14T03:15:20Z
**Site Type**: platform (confidence: 50%)

---

## Metrics

- **snr**: 24%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 76
- snr_percent: 24.06
- raw_tokens: 54303
- clean_tokens: 13063

### Semantic
- Score: 63
- semantic_tags_used: ['header', 'main', 'section', 'aside', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 127
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 13063
- estimated_cost_usd: 0.3919

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 188
- http_status: 200

### Api Availability
- Score: 45
- features: ['api_subdomain', 'api_docs', 'cli_tool']
- endpoints_found: ['https://api.ameblo.jp', 'https://ameblo.jp/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.