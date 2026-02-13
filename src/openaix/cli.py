"""CLI entry point for OpenAIX Scorer."""

import sys
import json
import argparse
from .scorer import OpenAIXScorer


def create_parser():
    parser = argparse.ArgumentParser(
        description='OpenAIX Scorer - Evaluate AI Experience (AIX) of websites',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python -m openaix https://example.com
  python -m openaix https://stripe.com/docs --pretty
  python -m openaix https://api.example.com --format md --output report.md
        '''
    )
    
    parser.add_argument('url', help='URL to evaluate')
    parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    parser.add_argument('-o', '--output', metavar='FILE', help='Save output to file')
    parser.add_argument('-f', '--format', choices=['json', 'md'], default='json', help='Output format')
    parser.add_argument('-t', '--timeout', type=int, default=10, help='Request timeout in seconds')
    
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    
    scorer = OpenAIXScorer(timeout=args.timeout)
    result = scorer.score(args.url)
    
    if args.format == 'md':
        output = generate_markdown_output(result)
    else:
        if args.pretty:
            output = json.dumps(result, indent=2, ensure_ascii=False)
        else:
            output = json.dumps(result, ensure_ascii=False)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"✅ Report saved to: {args.output}")
    else:
        print(output)


def generate_markdown_output(result: dict) -> str:
    lines = []
    lines.append(f"# OpenAIX Evaluation Report")
    lines.append(f"\n**URL:** {result['target']}")
    lines.append(f"**Score:** {result['score']}/100")
    lines.append(f"**Grade:** {result['grade']}")
    lines.append(f"**Timestamp:** {result['timestamp']}")
    lines.append(f"\n---\n")
    
    lines.append("## 📊 Metrics")
    metrics = result.get('metrics', {})
    for key, value in metrics.items():
        lines.append(f"- **{key}:** {value}")
    
    lines.append(f"\n---\n")
    lines.append("## 💡 Suggestions")
    for suggestion in result.get('suggestions', []):
        lines.append(f"- {suggestion}")
    
    return '\n'.join(lines)


if __name__ == '__main__':
    main()
