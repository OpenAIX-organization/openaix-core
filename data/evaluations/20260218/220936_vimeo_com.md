# OpenAIX Evaluation Report

**Target**: https://vimeo.com
**Score**: 45/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T14:09:36Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['graphql', 'api_subdomain', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 6
- snr_percent: 0.95
- raw_tokens: 594795
- clean_tokens: 5673

### Semantic
- Score: 60
- semantic_tags_used: ['nav', 'header', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 42
- heading_levels: 5
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 5673
- estimated_cost_usd: 0.1702

### Permissions
- Score: 50
- allowed_agents: ['ChatGPT-User', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'Google-Extended']
- llms_txt_present: False
- response_time_ms: 165
- http_status: 200

### Api Availability
- Score: 55
- features: ['graphql', 'api_subdomain', 'cli_tool']
- endpoints_found: ['https://vimeo.com/graphql', 'https://api.vimeo.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.