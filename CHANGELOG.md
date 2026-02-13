# OpenAIX Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial GitHub release preparation
- Comprehensive documentation
- CI/CD pipeline

## [1.2.0] - 2026-02-13

### Changed
- **Significantly more lenient grading thresholds**
  - S: 85+ (was 90+)
  - A: 70+ (was 80+)
  - B: 55+ (was 70+)
  - C: 40+ (was 60+)
  - F: <40 (was <60)

- **Improved Hidden Gem detection**
  - Now requires JSON-LD richness > 1000 characters
  - Requires good content structure (h1 + meaningful text)
  - Better filtering to avoid false positives on low-quality sites

- **Enhanced Graceful Degradation detection**
  - Lowered meaningful text threshold to 50 characters
  - Added bonus for text-heavy sites (>1000 chars)
  - Better handling of pure text sites without semantic HTML

- **Relaxed Metadata Consistency checks**
  - Threshold lowered from 30% to 10% similarity
  - Title and h1 differences are now normal (different purposes)
  - Partial credit given when both exist but differ

- **More lenient Token Economy scoring**
  - Adjusted curve: 50%+ SNR = 100pts (was 60%+)
  - Better minimum scores for low-SNR sites
  - Hidden Gems get minimum 80 points regardless of SNR

### Fixed
- Paul Graham blog scoring: 21 → 47 (F → C)
- Python Docs scoring: 56 → 67 (F → B)
- Apple scoring: 54 → 75 (F → A)
- Reduced false positive Hidden Gems from 5 to 1

## [1.1.0] - 2026-02-13

### Added
- **Graceful Degradation dimension** (15%)
  - Detects SSR vs CSR
  - Checks content accessibility without JavaScript
  - Bonus for text-heavy sites

- **Metadata Consistency checks**
  - Compares title and h1 similarity
  - Detects potential SEO cloaking
  - Provides samples in reports

- **Hidden Gem detection**
  - Identifies sites with rich visual UI but excellent structured data
  - Minimum score boost to 90 for qualifying sites
  - Considers JSON-LD richness and content structure

- **LLM Native Boost**
  - Sites with llms.txt get minimum 80 points
  - Recognizes AI-first configurations

- **CLI improvements**
  - Pretty print option
  - Markdown output format
  - Philosophy notes in reports

### Changed
- **"Commercial Reality" philosophy**
  - No longer penalizes complex UI/UX
  - Focus on "Fast Lane" for AI agents
  - Encourages structured data instead of simplified HTML

### Fixed
- Various edge cases in robots.txt parsing
- Better error handling for network issues
- Improved text extraction from complex HTML

## [1.0.0] - 2026-02-13

### Added
- Initial implementation of OpenAIX Scorer
- Four scoring dimensions:
  - Permission & Accessibility (20%)
  - Token Economy (30%)
  - Semantic Structure (30%)
  - AI Native Features (20%)
- Command-line interface (`openaix.py`)
- Batch evaluation tool (`benchmark.py`)
- JSON and Markdown output formats
- Basic error handling
- robots.txt parsing
- JSON-LD detection
- tiktoken integration for token counting

### Technical
- Python 3.10+ support
- requests for HTTP operations
- BeautifulSoup4 for HTML parsing
- markdownify for content cleaning

## Roadmap

### [1.3.0] - Planned
- [ ] Headless browser support for JS-rendered content analysis
- [ ] Plugin system for custom scoring dimensions
- [ ] Web dashboard for visualization
- [ ] Caching layer for repeated evaluations
- [ ] Multi-language content optimization

### [2.0.0] - Future
- [ ] Machine learning-based content quality assessment
- [ ] Dynamic weight adjustment by site category
- [ ] Real-time monitoring and alerting
- [ ] API server mode
- [ ] Browser extension for instant scoring

[Unreleased]: https://github.com/openaix/openaix/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/openaix/openaix/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/openaix/openaix/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/openaix/openaix/releases/tag/v1.0.0
