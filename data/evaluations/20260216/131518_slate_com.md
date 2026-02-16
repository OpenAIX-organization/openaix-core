# OpenAIX Evaluation Report

**Target**: https://slate.com
**Score**: 48/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-16T05:15:18Z
**Site Type**: content (confidence: 45%)

---

## Metrics

- **snr**: 5%
- **token_cost**: High
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['graphql', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 28
- snr_percent: 4.65
- raw_tokens: 137707
- clean_tokens: 6399

### Semantic
- Score: 62
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 28
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 6399
- estimated_cost_usd: 0.192

### Permissions
- Score: 40
- allowed_agents: ['Google-Extended']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'PerplexityBot']
- llms_txt_present: False
- response_time_ms: 6
- http_status: 200

### Api Availability
- Score: 35
- features: ['graphql', 'cli_tool']
- endpoints_found: ['https://slate.com/graphql']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- 🔧 Needs significant improvements.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.