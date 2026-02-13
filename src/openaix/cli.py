"""CLI entry point for OpenAIX Scorer."""

import sys
import json
import argparse
from .scorer import OpenAIXScorer
from .storage import EvaluationStorage


def create_parser():
    parser = argparse.ArgumentParser(
        description='OpenAIX Scorer - Evaluate AI Experience (AIX) of websites',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python -m openaix https://example.com
  python -m openaix https://stripe.com/docs --pretty
  python -m openaix https://api.example.com --format md --output report.md
  python -m openaix https://example.com --date 20260213
        '''
    )
    
    parser.add_argument('url', help='URL to evaluate')
    parser.add_argument('-p', '--pretty', action='store_true', help='Pretty print JSON output')
    parser.add_argument('-o', '--output', metavar='FILE', help='Save output to file (optional, defaults to data/evaluations/YYYYMMDD/)')
    parser.add_argument('-f', '--format', choices=['json', 'md'], default='json', help='Output format')
    parser.add_argument('-t', '--timeout', type=int, default=10, help='Request timeout in seconds')
    parser.add_argument('-d', '--date', metavar='YYYYMMDD', help='Date for evaluation folder (default: today)')
    parser.add_argument('--no-save', action='store_true', help='Do not save to data/evaluations/')
    
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    
    scorer = OpenAIXScorer(timeout=args.timeout)
    result = scorer.score(args.url)
    
    # Generate output
    if args.format == 'md':
        output = generate_markdown_output(result)
    else:
        if args.pretty:
            output = json.dumps(result, indent=2, ensure_ascii=False)
        else:
            output = json.dumps(result, ensure_ascii=False)
    
    # Save or print
    if args.output:
        # Custom output file
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"✅ Report saved to: {args.output}")
    elif not args.no_save:
        # Auto-save to standardized location
        storage = EvaluationStorage(date=args.date)
        saved = storage.save_evaluation(result, formats=[args.format])
        
        if args.format == 'md' and 'md' in saved:
            print(f"✅ Report saved to: {saved['md']}")
        elif 'json' in saved:
            print(f"✅ Report saved to: {saved['json']}")
        
        # Also print to stdout
        print("\n" + output)
    else:
        # Just print
        print(output)


def generate_markdown_output(result: dict) -> str:
    lines = []
    lines.append(f"# OpenAIX Evaluation Report")
    lines.append(f"\n**URL:** {result['target']}")
    lines.append(f"**Score:** {result['score']}/100")
    lines.append(f"**Grade:** {result['grade']}")
    
    # Add site type info if available
    site_type = result.get('site_type', {})
    if site_type:
        lines.append(f"**Site Type:** {site_type.get('type', 'unknown')}")
    
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
