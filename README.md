# OpenAIX Scorer v2.0

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Status](https://img.shields.io/badge/status-alpha-orange)
![AIX](https://img.shields.io/badge/AIX-Standard-black)

> **"The Web was built for eyes. We are indexing it for minds."**

The **OpenAIX Scorer** evaluates websites based on their **AI Experience (AIX)** — measuring how effectively an AI Agent (LLM, RAG, Crawler) can retrieve and understand the content.

## 🧐 Why AIX?

Modern web development optimizes for Human UX (Visuals, Animations, Interactivity). This often creates a hostile environment for AI Agents:
- **High Noise**: HTML/CSS bloat wastes tokens ($$$).
- **Hallucinations**: Ambiguous data structures confuse LLMs.
- **Inaccessibility**: Content hidden behind client-side JS rendering.

**OpenAIX bridges the gap.** We help developers build "Hybrid Interfaces" — beautiful for humans, structured for machines.

## 📊 The 4 Core Dimensions

1. **Signal-to-Noise Ratio (SNR)**: 30%
   - Measures the density of semantic content vs. HTML boilerplate.

2. **Semantic Structure**: 30%
   - Checks for valid HTML5 semantic tags and JSON-LD metadata.

3. **Token Economy**: 20%
   - Calculates the cost for an LLM to "read" the page.

4. **Agent Permissions**: 20%
   - Verifies `robots.txt`, `llms.txt`, and API accessibility.

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/OpenAIX/openaix-scorer.git
cd openaix-scorer

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### Usage

#### Command Line

```bash
# Score a single URL
python -m openaix https://stripe.com/docs

# Pretty print JSON output
python -m openaix https://example.com --pretty

# Generate Markdown report
python -m openaix https://example.com --format md --output report.md
```

#### Python API

```python
from openaix import OpenAIXScorer

scorer = OpenAIXScorer()
result = scorer.score("https://stripe.com/docs")

print(f"Score: {result['score']}/100")
print(f"Grade: {result['grade']}")
print(f"SNR: {result['dimensions']['snr']['snr_percent']:.1f}%")
```

#### Batch Evaluation

```bash
# Evaluate multiple URLs
python benchmark.py https://example.com https://test.com

# Evaluate from file
python benchmark.py --urls-file urls.txt --output output/report.md
```

### Sample Output

```json
{
  "target": "https://stripe.com/docs",
  "score": 75,
  "grade": "Class A (Agent Friendly)",
  "class": "Agent Friendly",
  "metrics": {
    "snr": "35%",
    "token_cost": "Low",
    "json_ld": true,
    "llms_txt": false
  },
  "dimensions": {
    "snr": {"score": 85, "snr_percent": 35.2, ...},
    "semantic": {"score": 72, "json_ld_present": true, ...},
    "token_economy": {"score": 100, "cost_rating": "Low", ...},
    "permissions": {"score": 90, "llms_txt_present": false, ...}
  },
  "suggestions": [
    "✅ Agent Friendly. Good structure and low noise.",
    "📋 Add JSON-LD structured data to improve AI comprehension."
  ],
  "timestamp": "2026-02-13T16:30:00Z",
  "version": "2.0.0"
}
```

## 🏆 Scoring Classes

| Class | Score Range | Description |
| :--- | :--- | :--- |
| **S** | 85-100 | **Silicon Native**. Excellent for AI agents. |
| **A** | 70-84 | **Agent Friendly**. Good semantics, low noise. |
| **B** | 50-69 | **Acceptable**. Works for agents but could improve. |
| **C** | < 50 | **Needs Improvement**. Significant barriers for AI. |

## 📁 Project Structure

```
openaix-scorer/
├── src/openaix/           # Main package
│   ├── __init__.py
│   ├── scorer.py          # Main scorer class
│   ├── cli.py             # Command line interface
│   ├── dimensions/        # Scoring dimensions
│   │   ├── snr.py         # Signal-to-Noise Ratio
│   │   ├── semantic.py    # Semantic Structure
│   │   ├── token.py       # Token Economy
│   │   └── permissions.py # Agent Permissions
│   └── utils/             # Utility functions
│       └── helpers.py
├── tests/                 # Test suite
├── docs/                  # Documentation
├── examples/              # Usage examples
├── output/                # Generated reports (gitignored)
└── benchmark.py           # Batch evaluation tool
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Found a site that scores incorrectly? [Open an Issue](https://github.com/OpenAIX/openaix-scorer/issues).
- Want to propose a new metric? Submit an RFC.

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## 📜 License

MIT © [OpenAIX.org](https://openaix.org)
