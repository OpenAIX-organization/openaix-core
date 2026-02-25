# OpenAIX Evaluation Report

**Target**: https://abs.gov.au
**Score**: 54/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T18:15:32Z
**Site Type**: documentation (confidence: 25%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: False
- **llms_txt**: False
- **api_features**: ['api_docs', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 25
- snr_percent: 4.09
- raw_tokens: 52869
- clean_tokens: 2162

### Semantic
- Score: 61
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'aside', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 0
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 2162
- estimated_cost_usd: 0.0649

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: False
- response_time_ms: 27
- http_status: 200

### Api Availability
- Score: 25
- features: ['api_docs', 'cli_tool']
- endpoints_found: ['https://abs.gov.au/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📋 Add JSON-LD structured data for better AI understanding.
- 📝 Add /llms.txt to describe your site for AI agents.