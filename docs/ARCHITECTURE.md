# Architecture Design

## Overview

OpenAIX Scorer is a Python-based web service evaluation tool that assesses how "friendly" a website is for AI Agents (LLMs, RAG systems, and crawlers).

## Philosophy

**"Commercial Reality"**: Modern websites should not be penalized for having rich visual experiences (React, CSS animations, complex UI). As long as the website provides a "Fast Lane" for AI agents through structured data, semantic markup, or dedicated AI configuration files, it should score well.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Input                            │
│                     (URL to evaluate)                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    OpenAIXScorer Class                       │
│                    (Main Controller)                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
           ┌───────────┼───────────┬───────────┬───────────┐
           │           │           │           │           │
           ▼           ▼           ▼           ▼           ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
    │Permission│ │ Graceful │ │  Token   │ │Semantic  │ │  AI      │
    │   &     │ │Degradation│ │ Economy  │ │Structure │ │ Native   │
    │   Access │ │          │ │          │ │          │ │ Features │
    └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘
         │            │            │            │            │
         └────────────┴────────────┴────────────┴────────────┘
                              │
                              ▼
              ┌─────────────────────────────┐
              │      Score Aggregation       │
              │    (Weighted Calculation)    │
              └──────────────┬──────────────┘
                             │
                             ▼
              ┌─────────────────────────────┐
              │    Report Generation         │
              │  (JSON/Markdown/Console)     │
              └─────────────────────────────┘
```

## Scoring Engine Flow

### 1. Permission & Accessibility (15%)

**Purpose**: Ensure the site is accessible to AI crawlers

**Checks**:
- robots.txt compliance
- HTTP response status
- Response time

**Implementation**:
```python
def check_permission(self, url: str) -> Dict[str, Any]:
    # 1. Fetch robots.txt
    # 2. Parse for AI agent rules
    # 3. Test main URL response
    # 4. Calculate accessibility score
```

**Scoring Logic**:
```
Base: 100
- Blocked agents: -15 per agent
- Slow response (>2s): -15
- Medium response (1-2s): -10
- Fast response (0.5-1s): -5
- 403/401 status: 0 (immediate fail)
```

### 2. Graceful Degradation (15%)

**Purpose**: Verify content is accessible without JavaScript execution

**Approach**: Simulate basic crawler (no JS support) and check content availability

**Key Indicators**:
- Meaningful text content (>50 chars)
- Presence of headings (h1-h3)
- No loading states
- Content structure visible

**Scoring Logic**:
```
Indicators (each worth ~16.67 points):
- has_meaningful_text: text_length > 50
- has_h1: present
- has_any_heading: h1/h2/h3 present
- has_main_content: main/article/section/div
- no_loading_state: no JS-required messages
- no_empty_body: HTML > 1000 chars

Bonus: +15 for text-heavy sites (>1000 chars)
```

### 3. Token Economy (25%)

**Purpose**: Measure content density and signal-to-noise ratio

**Calculation**:
```
SNR = (Clean Content Tokens / Raw HTML Tokens) × 100
```

**Process**:
1. Count tokens in raw HTML
2. Remove scripts, styles, hidden elements
3. Convert to Markdown (remove formatting)
4. Count clean content tokens
5. Calculate ratio

**v1.2 Scoring Curve**:
```
SNR ≥ 50%:  100 points
SNR 30-50%: 85 + (SNR - 30) × 0.5
SNR 15-30%: 70 + (SNR - 15)
SNR 5-15%:  50 + (SNR - 5) × 2
SNR < 5%:   SNR × 10
```

**Hidden Gem Exception**: If site is a Hidden Gem, minimum 80 points regardless of SNR

### 4. Semantic Structure (30%)

**Purpose**: Evaluate HTML semantic quality and metadata consistency

**Components**:

#### A. Semantic Tags (25%)
```python
semantic_tags = ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
score = (used_tags / total_tags) × 25
```

#### B. Heading Hierarchy (20%)
```python
if h1_present: +12 points
if 2+ heading levels: +8 points
```

#### C. JSON-LD Structured Data (25%)
```python
if rich_json_ld (>500 chars): +25 points
if basic_json_ld: +15 points
```

#### D. Image Accessibility (10%)
```python
score = (images_with_alt / total_images) × 10
```

#### E. Metadata Consistency (20%)
```python
similarity = text_similarity(title, h1)
if similarity > 10%: +20 points
elif both exist: +10 points (partial credit)
```

**Hidden Gem Detection**:
```python
is_hidden_gem = (
    text_density < 0.25 and           # Visual-heavy
    json_ld_richness > 1000 and       # Rich structured data
    has_good_structure and              # Basic content quality
    snr < 50                           # Low SNR (visual complexity)
)
# If Hidden Gem: minimum 90 points
```

### 5. AI Native Features (15%)

**Purpose**: Detect AI-specific optimizations

**Features**:
- `/llms.txt`: +50 points
- `/.well-known/ai-plugin.json`: +30 points

**LLM Native Boost**: If llms.txt present, minimum 80 points

## Data Flow

### Input Processing
1. URL normalization (add https:// if missing)
2. robots.txt parsing and caching
3. HTTP request with appropriate headers

### Analysis Pipeline
1. **Parallel dimension checks** where possible
2. **Dependency resolution** (some dimensions depend on others)
3. **Score aggregation** with weighted sum
4. **Post-processing** (Hidden Gem bonuses, LLM Native Boost)

### Output Generation
1. Calculate total score
2. Determine letter grade
3. Generate contextual summary
4. Create actionable suggestions
5. Format output (JSON/Markdown)

## Key Algorithms

### Text Similarity Calculation
```python
def text_similarity(text1: str, text2: str) -> float:
    words1 = extract_words(text1.lower())
    words2 = extract_words(text2.lower())
    
    intersection = words1 ∩ words2
    union = words1 ∪ words2
    
    return len(intersection) / len(union)
```

### robots.txt Parsing
```python
def is_agent_blocked(robots_content: str, agent: str) -> bool:
    for line in robots_content:
        if line starts with 'user-agent:':
            current_agent = parse_agent(line)
        if line starts with 'disallow:' and current_agent matches:
            if path is '/':
                return True
    return False
```

### Token Counting
```python
def count_tokens(text: str) -> int:
    encoder = tiktoken.get_encoding("cl100k_base")
    return len(encoder.encode(text))
```

## Error Handling

### Graceful Degradation
- **Network timeouts**: Return partial scores with timeout indicator
- **Parse errors**: Continue with available data, flag in report
- **Missing resources**: Assume defaults (e.g., robots.txt 404 = allow all)

### Recovery Strategies
1. Retry failed requests (1 retry with exponential backoff)
2. Use fallback User-Agent if blocked
3. Cache intermediate results for batch processing

## Performance Considerations

### Optimization Techniques
1. **Connection pooling** via requests.Session()
2. **Parallel processing** for batch operations
3. **Timeout management** to prevent hanging
4. **Caching** for robots.txt and static resources

### Resource Limits
- Max HTML size: 10MB (configurable)
- Request timeout: 10s default
- Max concurrent connections: 3 (avoid overwhelming servers)

## Extension Points

### Adding New Dimensions
To add a new scoring dimension:

1. Add weight to `WEIGHTS` dictionary
2. Implement analysis method
3. Add to `score()` method
4. Update documentation
5. Add tests
6. Update benchmark suite

Example:
```python
# In OpenAIXScorer class
WEIGHTS = {
    # ... existing weights
    'new_dimension': 0.10,
}

def analyze_new_dimension(self, soup: BeautifulSoup) -> Dict[str, Any]:
    # Implementation
    return {'score': calculated_score, ...}

def score(self, url: str) -> Dict[str, Any]:
    # ... other dimensions
    new_result = self.analyze_new_dimension(soup)
    dimensions['new_dimension'] = new_result
    # ... rest of scoring
```

### Custom Scoring Rules
Implement custom rules by subclassing:

```python
class CustomScorer(OpenAIXScorer):
    def _calculate_grade(self, score: int) -> str:
        # Custom grading logic
        pass
```

## Security Considerations

### Input Validation
- Sanitize URLs before requests
- Limit request size
- Validate content types

### Safe Browsing
- Respect robots.txt
- Use reasonable request rates
- Include identifying User-Agent

## Future Enhancements

### Planned Features
1. **Headless browser support** for JS-rendered content analysis
2. **Caching layer** for repeated evaluations
3. **API server** mode for production use
4. **Plugin system** for custom checks
5. **Web dashboard** for visualization

### Research Areas
1. **ML-based content quality assessment**
2. **Dynamic weight adjustment** based on site type
3. **Multi-language support** optimization
4. **Accessibility integration** (WCAG compliance)

## References

- [llms.txt Specification](https://llmstxt.org/)
- [Schema.org](https://schema.org/)
- [Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html)
- [tiktoken documentation](https://github.com/openai/tiktoken)

## Version History

- **v1.0**: Initial implementation (4 dimensions, strict scoring)
- **v1.1**: Added Graceful Degradation, Metadata Consistency
- **v1.2**: Optimized scoring thresholds, improved Hidden Gem detection
