# OpenAIX Evaluation Report

**Target**: https://webmd.com
**Score**: 37/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-15T12:06:31Z
**Site Type**: platform (confidence: 63%)

---

## Metrics

- **snr**: 6%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 34
- snr_percent: 5.98
- raw_tokens: 120856
- clean_tokens: 7232

### Semantic
- Score: 50
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 42
- heading_levels: 2
- has_h1: False

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 7232
- estimated_cost_usd: 0.217

### Permissions
- Score: 60
- allowed_agents: ['anthropic-ai', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'ClaudeBot', 'ChatGPT-User']
- llms_txt_present: False
- response_time_ms: 171
- http_status: 200

### Api Availability
- Score: 10
- features: ['cli_tool']
- endpoints_found: []
- has_api: False
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.
- 🔌 As a platform, consider adding OpenAPI spec or API documentation.