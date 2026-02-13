## Release v1.2.0 - "Balanced Reality"

🎉 We're excited to announce OpenAIX v1.2.0, featuring significantly improved scoring thresholds and more accurate detection algorithms!

### 🎯 Key Improvements

#### More Lenient Grading
We've listened to community feedback and adjusted our grading scale to better reflect real-world website quality:

- **S**: 85+ (was 90+) - Exceptional sites
- **A**: 70+ (was 80+) - Excellent sites  
- **B**: 55+ (was 70+) - Good sites
- **C**: 40+ (was 60+) - Acceptable sites
- **F**: <40 (was <60) - Sites needing improvement

This change better reflects the reality that most commercial sites are doing reasonable work for AI accessibility.

#### Improved Hidden Gem Detection
- **Stricter criteria**: Now requires JSON-LD richness > 1000 characters
- **Better filtering**: Reduces false positives on low-quality sites
- **Content quality check**: Requires good structure (h1 + meaningful text)
- **Result**: Reduced false positives from 5 to 1 in our test suite

#### Enhanced Graceful Degradation
- Lowered meaningful text threshold to 50 characters
- Added bonus for text-heavy sites (>1000 chars)
- Better handling of pure text sites without semantic HTML
- Paul Graham blog: 21 → 47 (F → C)

#### Relaxed Metadata Consistency
- Threshold lowered from 30% to 10% similarity
- Recognizes that title and h1 serve different purposes
- Partial credit when both exist but differ

### 📊 Benchmark Results

**v1.1 vs v1.2 Comparison:**

| Metric | v1.1 | v1.2 | Change |
|--------|------|------|--------|
| Average Score | 43.4 | 51.4 | +8.0 |
| A Grades | 0 | 3 | +3 |
| B Grades | 0 | 2 | +2 |
| C Grades | 1 | 7 | +6 |
| F Grades | 13 | 2 | -11 |

**Top Performers:**
- Shopify: 76 (A) - Excellent structured data + SSR
- Apple: 75 (A) - Hidden Gem: Rich UI + JSON-LD
- Notion: 70 (A) - Good SSR + llms.txt
- Python Docs: 67 (B) - Clean semantic HTML
- Linear: 60 (B) - Good SSR + llms.txt

### 🛠️ Technical Changes

- More lenient Token Economy scoring curve
- Hidden Gems get minimum 80 points for Token Economy
- Better handling of table-based layouts (old school HTML)
- Improved robots.txt parsing
- Better error handling for network issues

### 📚 Documentation

- Added comprehensive [Architecture Guide](docs/ARCHITECTURE.md)
- Added complete [API Reference](docs/API.md)
- Updated [Contributing Guide](CONTRIBUTING.md)
- Added [Code of Conduct](CODE_OF_CONDUCT.md)

### 🧪 Testing

- Added pytest test suite in `tests/`
- CI/CD pipeline with GitHub Actions
- Coverage reporting with Codecov
- Automated benchmark testing

### 🙏 Contributors

Special thanks to everyone who provided feedback and helped shape v1.2!

### 🗺️ What's Next?

**v1.3 Planned Features:**
- Headless browser support for JS-rendered content
- Plugin system for custom scoring dimensions
- Web dashboard for visualization

**v2.0 Future Vision:**
- ML-based content quality assessment
- Real-time monitoring and alerting
- API server mode

### 📦 Installation

```bash
pip install openaix
```

### 🚀 Quick Start

```bash
# Score a website
python openaix.py https://example.com --pretty

# Run benchmark
python benchmark.py --urls-file urls.txt --output report.md
```

### 📞 Support

- GitHub Issues: https://github.com/openaix/openaix/issues
- GitHub Discussions: https://github.com/openaix/openaix/discussions
- Documentation: https://openaix.org/docs

---

**Full Changelog**: https://github.com/openaix/openaix/compare/v1.1.0...v1.2.0
