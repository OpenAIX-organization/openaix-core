#!/usr/bin/env python3
"""OpenAIX Benchmark Tool - Batch website evaluation with standardized storage."""

import sys
import json
import argparse
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import List, Dict, Any

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from openaix import OpenAIXScorer
from openaix.storage import EvaluationStorage


def create_parser():
    parser = argparse.ArgumentParser(
        description='OpenAIX Benchmark - Batch website evaluation with standardized storage',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python benchmark.py https://example.com https://test.com
  python benchmark.py --urls-file test_urls.txt
  python benchmark.py --urls-file urls.txt --parallel 3
  python benchmark.py --urls-file urls.txt --date 20260213
        '''
    )
    
    parser.add_argument('urls', nargs='*', help='URLs to evaluate (space-separated)')
    parser.add_argument('-f', '--urls-file', metavar='FILE', help='File containing URLs (one per line)')
    parser.add_argument('-o', '--output', metavar='FILE', help='Output file (optional, defaults to data/evaluations/YYYYMMDD/)')
    parser.add_argument('-p', '--parallel', type=int, default=3, help='Number of parallel workers')
    parser.add_argument('-t', '--timeout', type=int, default=10, help='Request timeout per URL')
    parser.add_argument('-d', '--date', metavar='YYYYMMDD', help='Date for evaluation folder (default: today)')
    parser.add_argument('--json', action='store_true', help='Also save results as JSON')
    parser.add_argument('--no-save', action='store_true', help='Do not save individual evaluation files')
    
    return parser


def load_urls(args) -> List[str]:
    urls = []
    
    if args.urls:
        urls.extend(args.urls)
    
    if args.urls_file:
        try:
            with open(args.urls_file, 'r') as f:
                file_urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                urls.extend(file_urls)
        except FileNotFoundError:
            print(f"❌ Error: File not found: {args.urls_file}")
            sys.exit(1)
    
    seen = set()
    unique_urls = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)
    
    return unique_urls


def score_single_url(scorer: OpenAIXScorer, url: str) -> Dict[str, Any]:
    try:
        result = scorer.score(url)
        return {
            'success': True,
            'url': url,
            'result': result
        }
    except Exception as e:
        return {
            'success': False,
            'url': url,
            'error': str(e)
        }


def detect_anomalies(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Detect anomalies in results using correct dimension names."""
    anomalies = []
    
    for item in results:
        if not item.get('success'):
            continue
        
        result = item['result']
        dims = result.get('dimensions', {})
        
        # Anomaly 1: Hidden Gem (low SNR but high semantic score)
        snr = dims.get('snr', {}).get('snr_percent', 100)
        sem_score = dims.get('semantic', {}).get('score', 0)
        hidden_gem = dims.get('semantic', {}).get('hidden_gem', False)
        
        if snr < 40 and sem_score > 80 and hidden_gem:
            anomalies.append({
                'type': 'HIDDEN_GEM',
                'url': result['target'],
                'description': 'Rich visual UI with excellent structured data',
                'details': {'snr': snr, 'semantic_score': sem_score}
            })
        
        # Anomaly 2: High score but blocked agents
        total = result.get('score', 0)
        blocked = dims.get('permissions', {}).get('blocked_agents', [])
        
        if total > 70 and len(blocked) > 2:
            anomalies.append({
                'type': 'HIGH_SCORE_BLOCKED',
                'url': result['target'],
                'description': 'High score but some AI agents blocked in robots.txt',
                'details': {'total_score': total, 'blocked_agents': blocked}
            })
    
    return anomalies


def generate_markdown_report(results: List[Dict[str, Any]], anomalies: List[Dict[str, Any]]) -> str:
    """Generate markdown report using correct dimension names."""
    lines = []
    
    lines.append("# OpenAIX Benchmark Report v2.0")
    lines.append(f"\n**Generated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    lines.append(f"\n---\n")
    
    successful = [r for r in results if r.get('success')]
    failed = [r for r in results if not r.get('success')]
    
    if successful:
        scores = [r['result']['score'] for r in successful]
        grades = [r['result']['grade'] for r in successful]
        
        avg_score = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        
        grade_counts = {}
        for g in grades:
            grade_class = g[6] if len(g) > 6 else '?'
            grade_counts[grade_class] = grade_counts.get(grade_class, 0) + 1
        
        lines.append("## 📊 Summary Statistics")
        lines.append(f"\n- **Total URLs:** {len(results)}")
        lines.append(f"- **Successful:** {len(successful)}")
        lines.append(f"- **Failed:** {len(failed)}")
        lines.append(f"- **Average Score:** {avg_score:.1f}")
        lines.append(f"- **Highest:** {max_score}")
        lines.append(f"- **Lowest:** {min_score}")
        lines.append(f"\n**Grade Distribution:**")
        for grade in ['S', 'A', 'B', 'C']:
            count = grade_counts.get(grade, 0)
            bar = '█' * count
            lines.append(f"- {grade}: {count} {bar}")
    
    # Hidden Gems
    hidden_gems = [a for a in anomalies if a['type'] == 'HIDDEN_GEM']
    if hidden_gems:
        lines.append("\n---\n")
        lines.append("## ⭐ Hidden Gems Detected")
        lines.append("\n*Sites with rich visual UI and excellent structured data:*")
        lines.append("")
        for gem in hidden_gems:
            lines.append(f"- **{gem['url']}** - {gem['description']}")
    
    # All Results Table
    lines.append("\n---\n")
    lines.append("## 📋 Detailed Results")
    lines.append("")
    lines.append("| URL | Score | Grade | SNR | Token | Semantic | Permissions |")
    lines.append("|-----|-------|-------|-----|-------|----------|-------------|")
    
    for item in results:
        if not item.get('success'):
            url = item['url'][:50]
            lines.append(f"| {url}... | ERROR | - | - | - | - | - |")
            continue
        
        result = item['result']
        dims = result.get('dimensions', {})
        url = result['target'][:40] + ('...' if len(result['target']) > 40 else '')
        
        snr = dims.get('snr', {}).get('score', 0)
        token = dims.get('token_economy', {}).get('score', 0)
        semantic = dims.get('semantic', {}).get('score', 0)
        permissions = dims.get('permissions', {}).get('score', 0)
        grade_letter = result['grade'][6] if len(result['grade']) > 6 else '?'
        
        lines.append(f"| {url} | {result['score']} | {grade_letter} | {snr} | {token} | {semantic} | {permissions} |")
    
    # Top Performers
    if successful:
        lines.append("\n---\n")
        lines.append("## 🏆 Top Performers")
        lines.append("")
        
        top = sorted(successful, key=lambda x: x['result']['score'], reverse=True)[:5]
        for i, item in enumerate(top, 1):
            r = item['result']
            grade_letter = r['grade'][6] if len(r['grade']) > 6 else '?'
            lines.append(f"{i}. **{r['target']}** - {r['score']}/100 ({grade_letter})")
            if r.get('suggestions'):
                lines.append(f"   - {r['suggestions'][0]}")
    
    # Footer
    lines.append("\n---\n")
    lines.append("*Report generated by OpenAIX Benchmark v2.0*")
    
    return '\n'.join(lines)


def main():
    parser = create_parser()
    args = parser.parse_args()
    
    urls = load_urls(args)
    
    if not urls:
        print("❌ Error: No URLs provided. Use positional arguments or --urls-file")
        sys.exit(1)
    
    print(f"🔍 OpenAIX Benchmark v2.1")
    print(f"📊 Evaluating {len(urls)} URLs with {args.parallel} parallel workers\n")
    
    # Initialize storage
    storage = EvaluationStorage(custom_date=args.date)
    print(f"💾 Storage: {storage.get_storage_path()}/\n")
    
    scorer = OpenAIXScorer(timeout=args.timeout)
    
    results = []
    completed = 0
    failed = 0
    
    with ThreadPoolExecutor(max_workers=args.parallel) as executor:
        future_to_url = {
            executor.submit(score_single_url, scorer, url): url 
            for url in urls
        }
        
        for future in as_completed(future_to_url):
            result = future.result()
            results.append(result)
            
            if result['success']:
                completed += 1
                r = result['result']
                grade_letter = r['grade'][6] if len(r['grade']) > 6 else '?'
                print(f"✅ [{completed}/{len(urls)}] {r['target'][:50]}... - {r['score']}/100 ({grade_letter})")
                
                # Save individual evaluation
                if not args.no_save:
                    saved_files = storage.save_evaluation(
                        r, 
                        formats=['json', 'md'] if args.json else ['json']
                    )
            else:
                failed += 1
                print(f"❌ [{completed + failed}/{len(urls)}] {result['url'][:50]}... - ERROR: {result.get('error', 'Unknown')}")
    
    results.sort(key=lambda x: urls.index(x['url']) if x['url'] in urls else 999)
    
    print("\n🔍 Detecting anomalies...")
    anomalies = detect_anomalies(results)
    if anomalies:
        print(f"   Found {len(anomalies)} anomalies")
        for a in anomalies:
            if a['type'] == 'HIDDEN_GEM':
                print(f"   ⭐ Hidden Gem: {a['url']}")
    else:
        print("   No anomalies detected")
    
    # Generate summary report
    print(f"\n📝 Generating summary report...")
    report = generate_markdown_report(results, anomalies)
    
    # Save summary report
    if args.output:
        # Custom output path
        output_dir = os.path.dirname(args.output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        summary_path = args.output
    else:
        # Default to storage directory
        timestamp = datetime.now().strftime('%H%M%S')
        summary_path = os.path.join(storage.get_storage_path(), f"{timestamp}_summary.md")
    
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"✅ Summary report saved to: {summary_path}")
    
    # Save JSON summary
    json_path = summary_path.replace('.md', '.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"✅ JSON data saved to: {json_path}")
    
    successful = [r for r in results if r.get('success')]
    if successful:
        scores = [r['result']['score'] for r in successful]
        avg = sum(scores) / len(scores)
        print(f"\n" + "="*60)
        print(f"📊 Benchmark Complete")
        print(f"="*60)
        print(f"Total URLs: {len(urls)}")
        print(f"Successful: {len(successful)}")
        print(f"Failed: {failed}")
        print(f"Average Score: {avg:.1f}")
        print(f"Storage: {storage.get_storage_path()}/")
    
    print("\n✨ Done!")


if __name__ == '__main__':
    main()
