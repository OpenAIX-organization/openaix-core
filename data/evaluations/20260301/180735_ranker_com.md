# OpenAIX Evaluation Report

**Target**: https://ranker.com
**Score**: 54/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-03-01T10:07:35Z
**Site Type**: content (confidence: 46%)

---

## Metrics

- **snr**: 4%
- **token_cost**: Medium
- **json_ld**: True
- **llms_txt**: False
- **api_features**: ['api_subdomain', 'cli_tool']
- **api_endpoints**: 1

---

## Dimensions


### Snr
- Score: 26
- snr_percent: 4.26
- raw_tokens: 132174
- clean_tokens: 5633

### Semantic
- Score: 65
- semantic_tags_used: ['article', 'nav', 'header', 'section', 'footer']
- json_ld_present: True
- hidden_gem: False
- images_total: 83
- heading_levels: 0
- has_h1: False

### Token Economy
- Score: 85
- cost_rating: Medium
- clean_tokens: 5633
- estimated_cost_usd: 0.169

### Permissions
- Score: 60
- allowed_agents: ['ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot']
- llms_txt_present: False
- response_time_ms: 47
- http_status: 200

### Api Availability
- Score: 30
- features: ['api_subdomain', 'cli_tool']
- endpoints_found: ['https://api.ranker.com']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ⚠️ Class B - Human Optimized. Top 50%, room to improve.
- 📉 Low SNR: Consider SSR or reducing JS dependencies.
- 📝 Add /llms.txt to describe your site for AI agents.