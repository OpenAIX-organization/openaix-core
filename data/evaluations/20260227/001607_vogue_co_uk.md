# OpenAIX Evaluation Report

**Target**: https://vogue.co.uk
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-26T16:16:07Z
**Site Type**: content (confidence: 100%)

---

## Metrics

- **snr**: 1%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['cli_tool']
- **api_endpoints**: 0

---

## Dimensions


### Snr
- Score: 6
- snr_percent: 1.07
- raw_tokens: 354814
- clean_tokens: 3779

### Semantic
- Score: 71
- semantic_tags_used: ['nav', 'header', 'main', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 30
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 3779
- estimated_cost_usd: 0.1134

### Permissions
- Score: 60
- allowed_agents: ['GPTBot', 'anthropic-ai', 'ChatGPT-User']
- blocked_agents: ['CCBot', 'ClaudeBot', 'Google-Extended', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 62
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
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.