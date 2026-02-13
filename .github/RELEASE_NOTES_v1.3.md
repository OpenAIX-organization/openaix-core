## Release v1.3.0 - "Code Review Fixes"

🛠️ **Critical bug fixes based on thorough code review**

### 🚨 Critical Fixes

#### 1. Fixed robots.txt Parser (CRITICAL)
**Problem**: Custom parser had serious flaws:
- Only checked `Disallow: /` (root), ignored partial path blocking
- Didn't handle `Allow:` directives (modern websites use these)
- String matching bugs (e.g., `CCBot` matched `CCBot-Extended`)
- No wildcard support

**Fix**: Now uses Python's standard `urllib.robotparser` library
- Correctly handles Allow/Disallow precedence
- Respects standard robots.txt specification
- Proper agent matching

**Impact**: Previously, many sites were incorrectly flagged as blocking AI agents.

#### 2. Fixed Content Accessibility Detection (MAJOR)
**Problem**: 
- Method named "Graceful Degradation" but didn't actually detect SSR vs CSR
- Just changed User-Agent, which doesn't change server response
- `has_main_content` checked for `<div>` (every page has this)

**Fix**: 
- Renamed to `check_content_accessibility()` (more honest)
- Now focuses on **content quality** heuristics
- Word count, heading structure, paragraph count
- Added honesty note: "True SSR detection requires headless browser"

#### 3. Improved Token Economy (MINOR)
**Fix**: Now removes SVG and `<template>` elements in addition to scripts/styles
- SVG was bloating SNR for icon-heavy sites
- `<template>` tags (used by modern frameworks) now removed

#### 4. Improved Hidden Gem Detection (MINOR)
**Fix**: Now validates JSON-LD quality, not just length
- Checks for required fields (`@type`, `name`, `description`)
- Validates JSON structure
- Reduces false positives

### 🛡️ Reliability Improvements

#### Error Handling
- Added proper logging with `logging` module
- All network requests now have try/except with logging
- Errors are logged at appropriate levels (INFO, WARNING, ERROR)
- No more silent failures

#### Rate Limiting
- Added `rate_limit` parameter (default: 1 req/sec)
- Prevents overwhelming target servers
- Respects web etiquette
- Configurable for batch processing

#### Transparency
- Added explicit `THRESHOLDS` dictionary
- All magic numbers now documented
- Added honesty note in output: "Weights are heuristic"
- Added note: "Results are directional guidance, not absolute truth"

### 📝 Documentation Updates

- Added comprehensive `CODE_REVIEW.md` document
- Honest assessment of limitations
- Future improvement roadmap
- Acknowledges this is research software

### ⚠️ Known Limitations (Documented)

1. **True SSR vs CSR detection requires headless browser** - current method is heuristic
2. **Weights are heuristic** - not based on formal LLM performance research
3. **Token economy uses GPT-4 tokenizer** - other models may differ
4. **robots.txt is advisory** - not all crawlers follow it

### 📊 Version Comparison

```
v1.2: Average score 51.4, mostly working
v1.3: More correct, honest about limitations
```

### 🧪 Testing

- All existing tests pass
- Added more edge case handling
- Better mock support

### 🙏 Thanks

Special thanks to the critical code review that identified these issues before open sourcing!

### 🗺️ What's Next?

**v1.4 Planned**:
- Headless browser option for true SSR detection
- Plugin system for custom dimensions
- More comprehensive test suite

**v2.0 Vision**:
- Evidence-based weights from LLM performance testing
- Machine learning scoring model
- Web dashboard

### 📦 Installation

```bash
pip install openaix
```

### 🚀 Quick Start

```python
from openaix_scorer import OpenAIXScorer

# Default: 1 req/sec rate limiting
scorer = OpenAIXScorer()

# Faster for batch processing (be careful!)
scorer = OpenAIXScorer(rate_limit=0.5)  # 2 req/sec

result = scorer.score("https://example.com")
print(f"Score: {result['total_score']}/100")
```

**Full Changelog**: https://github.com/openaix/openaix/compare/v1.2.0...v1.3.0
