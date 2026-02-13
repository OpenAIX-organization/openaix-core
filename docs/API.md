# API Documentation

## Python API

### OpenAIXScorer Class

The main interface for scoring websites.

#### Constructor

```python
from openaix_scorer import OpenAIXScorer

scorer = OpenAIXScorer(timeout: int = 10)
```

**Parameters:**
- `timeout` (int): HTTP request timeout in seconds (default: 10)

#### Methods

##### `score(url: str) -> Dict[str, Any]`

Score a website and return a complete report.

**Parameters:**
- `url` (str): The URL to evaluate

**Returns:**
A dictionary containing the complete scoring report.

**Example:**
```python
from openaix_scorer import OpenAIXScorer

scorer = OpenAIXScorer()
result = scorer.score("https://example.com")

print(f"Score: {result['total_score']}/100")
print(f"Grade: {result['grade']}")
```

**Response Structure:**
```json
{
  "url": "https://example.com",
  "total_score": 75,
  "grade": "A",
  "summary": "Good AI experience",
  "dimensions": {
    "permission_accessibility": {
      "score": 85,
      "allowed_agents": ["GPTBot", "ClaudeBot"],
      "blocked_agents": [],
      "response_time_ms": 245,
      "http_status": 200
    },
    "graceful_degradation": {
      "score": 90,
      "is_ssr": true,
      "text_length": 5000,
      "indicators": {...}
    },
    "token_economy": {
      "score": 70,
      "raw_html_tokens": 15000,
      "clean_content_tokens": 4500,
      "snr_percent": 30.0
    },
    "semantic_structure": {
      "score": 80,
      "semantic_tags_used": ["article", "nav", "header"],
      "json_ld_present": true,
      "hidden_gem": {...}
    },
    "ai_native": {
      "score": 80,
      "features": {
        "llms_txt_present": true,
        "ai_plugin_present": false
      },
      "llm_native_boost_applied": true
    }
  },
  "suggestions": [...],
  "philosophy_note": "...",
  "timestamp": "2026-02-13T12:00:00Z",
  "version": "1.2"
}
```

##### `check_permission(url: str) -> Dict[str, Any]`

Check permission and accessibility metrics.

**Returns:**
```python
{
  "score": int,              # 0-100
  "allowed_agents": list,    # List of allowed AI agent names
  "blocked_agents": list,    # List of blocked AI agent names
  "response_time_ms": int,   # Response time in milliseconds
  "http_status": int,        # HTTP status code
  "note": str                # Optional explanation
}
```

##### `check_graceful_degradation(url: str) -> Dict[str, Any]`

Check if content works without JavaScript.

**Returns:**
```python
{
  "score": int,              # 0-100
  "is_ssr": bool,            # True if server-side rendered
  "indicators": {
    "has_meaningful_text": bool,
    "has_h1": bool,
    "has_any_heading": bool,
    "has_main_content": bool,
    "no_loading_state": bool,
    "no_empty_body": bool
  },
  "text_length": int,
  "note": str
}
```

##### `analyze_token_economy(html: str) -> Dict[str, Any]`

Analyze HTML token economy.

**Parameters:**
- `html` (str): Raw HTML content

**Returns:**
```python
{
  "score": int,                    # 0-100
  "raw_html_tokens": int,
  "clean_content_tokens": int,
  "snr_percent": float,            # Signal-to-noise ratio
  "note": str
}
```

##### `analyze_semantic_structure(soup: BeautifulSoup, snr: float) -> Dict[str, Any]`

Analyze semantic HTML structure.

**Parameters:**
- `soup` (BeautifulSoup): Parsed HTML
- `snr` (float): Signal-to-noise ratio percentage

**Returns:**
```python
{
  "score": int,
  "semantic_tags_used": list,      # e.g., ["article", "nav"]
  "heading_levels": int,
  "json_ld_present": bool,
  "json_ld_richness": int,         # Character count
  "metadata_consistency": {
    "is_consistent": bool,
    "title_h1_similarity": float,
    "has_title": bool,
    "has_h1": bool,
    "samples": {...}
  },
  "hidden_gem": {
    "is_hidden_gem": bool,
    "text_density": float,
    "json_ld_richness": int,
    "message": str
  }
}
```

##### `check_ai_native_features(url: str) -> Dict[str, Any]`

Check for AI-native features.

**Returns:**
```python
{
  "score": int,
  "features": {
    "llms_txt_present": bool,
    "ai_plugin_present": bool
  },
  "llm_native_boost_applied": bool
}
```

## Command Line Interface

### `openaix.py`

Score a single URL.

#### Usage

```bash
python openaix.py <url> [options]
```

#### Options

- `-p, --pretty`: Pretty print JSON output
- `-o, --output FILE`: Save output to file
- `-f, --format {json,md}`: Output format (default: json)
- `-t, --timeout SECONDS`: Request timeout (default: 10)

#### Examples

```bash
# Basic usage
python openaix.py https://example.com

# Pretty print to console
python openaix.py https://example.com --pretty

# Save as JSON
python openaix.py https://example.com --output report.json

# Generate Markdown report
python openaix.py https://example.com --format md --output report.md
```

### `benchmark.py`

Batch evaluation tool.

#### Usage

```bash
python benchmark.py [urls...] [options]
```

#### Options

- `-f, --urls-file FILE`: File containing URLs (one per line)
- `-o, --output FILE`: Output file (default: benchmark_report.md)
- `-p, --parallel N`: Number of parallel workers (default: 3)
- `-t, --timeout SECONDS`: Request timeout per URL (default: 10)
- `--json`: Also save results as JSON

#### Examples

```bash
# Evaluate multiple URLs
python benchmark.py https://example.com https://test.com

# Evaluate from file
python benchmark.py --urls-file urls.txt

# Custom parallel workers
python benchmark.py --urls-file urls.txt --parallel 5 --output report.md
```

#### URL File Format

Create a text file with one URL per line:

```
# Comments start with #
https://example.com
https://test.com
https://another-site.org
```

## Scoring Dimensions

### Permission & Accessibility (15%)

Evaluates basic accessibility for AI crawlers.

**Scoring Factors:**
- robots.txt blocking status
- HTTP response time
- HTTP status codes

**Grade Thresholds:**
- 90-100: Fully accessible
- 70-89: Minor restrictions
- 50-69: Some limitations
- <50: Significant barriers

### Graceful Degradation (15%)

Checks if content is accessible without JavaScript.

**Key Metrics:**
- Text content availability
- Heading structure
- Loading states
- Content structure

**Interpretation:**
- 80-100: Excellent SSR
- 60-79: Good SSR with some dynamic content
- 40-59: Partial SSR
- <40: JS-dependent

### Token Economy (25%)

Measures content density vs HTML overhead.

**Calculation:**
```
SNR = (Clean Content Tokens / Raw HTML Tokens) × 100
```

**Scoring:**
- 50%+ SNR: Excellent (100 pts)
- 30-50%: Good (85-100 pts)
- 15-30%: Acceptable (70-85 pts)
- 5-15%: Below average (50-70 pts)
- <5%: Poor (0-50 pts)

### Semantic Structure (30%)

Evaluates HTML semantic quality.

**Components:**
1. Semantic tags (25%)
2. Heading hierarchy (20%)
3. JSON-LD structured data (25%)
4. Image accessibility (10%)
5. Metadata consistency (20%)

**Hidden Gem Bonus:**
If a site has rich visual UI (low SNR) but excellent JSON-LD, it receives a minimum score of 90.

### AI Native Features (15%)

Detects AI-specific optimizations.

**Features:**
- `/llms.txt`: +50 points
- `/.well-known/ai-plugin.json`: +30 points

**LLM Native Boost:**
Sites with llms.txt receive a minimum score of 80 for this dimension.

## Grading Scale

| Grade | Score Range | Interpretation |
|-------|-------------|----------------|
| S | 85-100 | Exceptional AI experience |
| A | 70-85 | Excellent AI experience |
| B | 55-70 | Good AI experience |
| C | 40-55 | Acceptable, needs improvement |
| F | <40 | Poor AI experience |

## Error Handling

### Common Errors

**TimeoutError**
```python
{
  "total_score": 0,
  "grade": "F",
  "summary": "Error: Request timeout",
  "suggestions": [...]
}
```

**ConnectionError**
```python
{
  "total_score": 0,
  "grade": "F",
  "summary": "Error: Failed to connect",
  ...
}
```

**ParseError**
Partial results with error flag:
```python
{
  "dimensions": {
    "permission_accessibility": {...},
    "graceful_degradation": {
      "score": 0,
      "note": "Error: Could not parse HTML"
    }
  }
}
```

## Best Practices

### For Library Users

1. **Handle timeouts gracefully:**
```python
from openaix_scorer import OpenAIXScorer

scorer = OpenAIXScorer(timeout=15)  # Increase for slow sites
try:
    result = scorer.score("https://slow-site.com")
except Exception as e:
    print(f"Scoring failed: {e}")
```

2. **Batch processing with rate limiting:**
```python
import time

urls = [...]  # List of URLs
results = []

for url in urls:
    result = scorer.score(url)
    results.append(result)
    time.sleep(1)  # Be nice to servers
```

3. **Custom scoring rules:**
```python
class StrictScorer(OpenAIXScorer):
    def _calculate_grade(self, score: int) -> str:
        # Stricter grading
        if score >= 90: return "S"
        if score >= 80: return "A"
        if score >= 65: return "B"
        if score >= 50: return "C"
        return "F"
```

### For Website Owners

1. **Check your score regularly:**
```bash
python openaix.py https://your-site.com --pretty
```

2. **Focus on suggestions:**
The `suggestions` field provides actionable improvements.

3. **Monitor changes:**
Track score changes after website updates.

## Integration Examples

### CI/CD Integration

```yaml
# .github/workflows/openaix.yml
name: OpenAIX Score Check
on: [push]

jobs:
  score:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install OpenAIX
        run: pip install openaix
      - name: Check Score
        run: |
          python -c "
          from openaix_scorer import OpenAIXScorer
          scorer = OpenAIXScorer()
          result = scorer.score('https://your-site.com')
          if result['total_score'] < 50:
              print(f'❌ Score too low: {result[\"total_score\"]}')
              exit(1)
          print(f'✅ Score: {result[\"total_score\"]}')
          "
```

### Webhook Integration

```python
from flask import Flask, request
from openaix_scorer import OpenAIXScorer

app = Flask(__name__)
scorer = OpenAIXScorer()

@app.route('/score', methods=['POST'])
def score_url():
    url = request.json.get('url')
    result = scorer.score(url)
    return result
```

## Versioning

The API follows semantic versioning:
- Major version changes may break compatibility
- Minor version changes add features
- Patch version changes fix bugs

Current version: **1.2.0**

## Support

For questions or issues:
- GitHub Issues: https://github.com/openaix/openaix/issues
- Documentation: https://openaix.org/docs
- Discussions: https://github.com/openaix/openaix/discussions
