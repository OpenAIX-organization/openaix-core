# OpenAIX Evaluation Report

**Target**: https://ibge.gov.br
**Score**: 63/100
**Grade**: Class C (Needs Improvement)
**Timestamp**: 2026-02-25T20:05:43Z
**Site Type**: platform (confidence: 100%)

---

## Metrics

- **snr**: 23%
- **token_cost**: High
- **json_ld**: False
- **llms_txt**: True
- **api_features**: ['graphql', 'api_docs', 'cli_tool']
- **api_endpoints**: 2

---

## Dimensions


### Snr
- Score: 75
- snr_percent: 23.4
- raw_tokens: 33945
- clean_tokens: 7944

### Semantic
- Score: 59
- semantic_tags_used: ['nav', 'header', 'main', 'section', 'footer']
- json_ld_present: False
- hidden_gem: False
- images_total: 24
- heading_levels: 4
- has_h1: True

### Token Economy
- Score: 65
- cost_rating: High
- clean_tokens: 7944
- estimated_cost_usd: 0.2383

### Permissions
- Score: 100
- allowed_agents: ['GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 'ChatGPT-User', 'Google-Extended', 'PerplexityBot']
- blocked_agents: []
- llms_txt_present: True
- response_time_ms: 667
- http_status: 200

### Api Availability
- Score: 50
- features: ['graphql', 'api_docs', 'cli_tool']
- endpoints_found: ['https://ibge.gov.br/graphql', 'https://ibge.gov.br/api']
- has_api: True
- has_comprehensive_api: False

---

## Suggestions

- ✅ Class A - Agent Friendly. Top 20% performance.
- 📋 Add JSON-LD structured data for better AI understanding.