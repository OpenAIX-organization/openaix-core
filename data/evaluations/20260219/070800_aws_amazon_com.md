# OpenAIX Evaluation Report

**Target**: https://aws.amazon.com
**Score**: 60/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-18T23:08:00Z
**Site Type**: platform (confidence: 36%)

---

## Metrics

- **snr**: 2%
- **token_cost**: Low
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 11
- snr_percent: 1.78
- raw_tokens: 105092
- clean_tokens: 1872

### Semantic
- Score: 64
- semantic_tags_used: ['nav', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 5
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 100
- cost_rating: Low
- clean_tokens: 1872
- estimated_cost_usd: 0.0562

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 215
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://aws.amazon.com/graphql', 'https://aws.amazon.com/developers']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Acceptable but has improvement opportunities.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.