# Contributing to OpenAIX

First off, thank you for considering contributing to OpenAIX! It's people like you that make this standard better for everyone.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to see if the problem has already been reported. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and what behavior you expected**
- **Include the URL(s) you were testing**
- **Include your environment details** (Python version, OS, etc.)

Example:
```
Title: False positive Hidden Gem detection on news sites

URL: https://example-news.com
Expected: Not marked as Hidden Gem (poor structured data)
Actual: Marked as Hidden Gem with score 90+
Python version: 3.12
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the enhancement**
- **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repository
2. Create a new branch from `main` for your feature or bug fix
3. Make your changes
4. Run the test suite to ensure nothing is broken
5. Update documentation if needed
6. Submit a pull request

#### Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
2. Update the README.md with details of changes to the interface, if applicable.
3. Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent.
4. Your Pull Request will be reviewed by maintainers. We may suggest changes or request clarification.

### Developing New Scoring Dimensions

If you want to propose a new scoring dimension:

1. Open an issue first to discuss the proposal
2. Explain the rationale and how it aligns with the "Commercial Reality" philosophy
3. Provide examples of websites that would score differently
4. Include weighting recommendations and justification

Example structure for new dimension proposals:
```markdown
## Proposal: [Dimension Name]

### Rationale
Why is this dimension important for AI accessibility?

### Scoring Criteria
- Criteria 1 (weight: X%)
- Criteria 2 (weight: Y%)

### Test Cases
- https://example.com should score X
- https://another.com should score Y

### Weight Recommendation
Recommended weight: Z%
Justification: [explanation]
```

## Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/openaix.git
cd openaix

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

## Style Guidelines

### Python Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with these specifics:

- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use type hints for function signatures
- Document all public methods with docstrings

Example:
```python
def analyze_semantic_structure(self, soup: BeautifulSoup, snr: float) -> Dict[str, Any]:
    """
    Analyze semantic HTML structure.
    
    Args:
        soup: BeautifulSoup object of the parsed HTML
        snr: Signal-to-noise ratio percentage
        
    Returns:
        Dictionary containing score and detailed metrics
    """
    # Implementation
```

### Commit Messages

Use clear and meaningful commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Improve Hidden Gem detection threshold

- Increase minimum JSON-LD size from 500 to 1000 chars
- Add check for meaningful content structure
- Fix false positives on news sites

Fixes #123
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=openaix_scorer --cov-report=html

# Run specific test file
pytest tests/test_scorer.py

# Run with verbose output
pytest -v
```

### Writing Tests

All new features should include tests. Tests should be:

- **Independent**: Each test should be able to run independently
- **Repeatable**: Tests should produce the same results every time
- **Clear**: Test names should describe what is being tested

Example:
```python
def test_hidden_gem_detection_requires_rich_jsonld():
    """Test that Hidden Gem requires substantial JSON-LD content."""
    scorer = OpenAIXScorer()
    # Test implementation
```

### Benchmark Testing

Before submitting changes that affect scoring:

1. Run the benchmark suite on the `test_urls.txt` list
2. Compare results with the baseline in `benchmark_report_v12.md`
3. Document any significant changes in your PR description

## Documentation

### Updating Documentation

When adding features or changing behavior:

1. Update the relevant docstrings
2. Update README.md if user-facing changes
3. Update CHANGELOG.md with a description of the change
4. Consider adding examples to the docs/ folder

### Documentation Style

- Use clear, concise language
- Include code examples where helpful
- Keep line length under 100 characters in Markdown files
- Use semantic line breaks (one sentence per line)

## Community

### Discussion

For general discussion and questions:
- Use GitHub Discussions for Q&A
- Use GitHub Issues for bugs and feature requests
- Be respectful and constructive in all interactions

### Recognition

Contributors will be recognized in our README.md and release notes.

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

Thank you for contributing to OpenAIX! 🚀
