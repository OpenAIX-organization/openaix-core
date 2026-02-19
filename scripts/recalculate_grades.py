#!/usr/bin/env python3
"""
Recalculate all historical grades using dynamic ranking system.
Updates all JSON files in data/evaluations/ with new grade information.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.openaix.dynamic_ranking import DynamicRanker


def recalculate_all_grades(history_dir: str = 'data/evaluations', dry_run: bool = False):
    """Recalculate grades for all historical evaluations."""
    
    print("=" * 60)
    print("OpenAIX Dynamic Ranking Recalculation")
    print("=" * 60)
    print()
    
    ranker = DynamicRanker(history_dir)
    
    # First, get current statistics
    print("📊 Current Statistics:")
    stats = ranker.get_statistics()
    print(f"   Total evaluations: {stats['total_evaluations']}")
    print(f"   Current thresholds:")
    for grade, info in stats['distribution'].items():
        print(f"     {grade}: {info['threshold']} ({info['count']} sites, {info['percent']})")
    print()
    
    # Find all evaluation files
    eval_files = []
    for root, dirs, files in os.walk(history_dir):
        for f in files:
            if f.endswith('.json'):
                eval_files.append(os.path.join(root, f))
    
    print(f"📝 Found {len(eval_files)} evaluation files")
    print()
    
    # Process each file
    updated_count = 0
    unchanged_count = 0
    error_count = 0
    
    grade_changes = {'S': 0, 'A': 0, 'B': 0, 'C': 0}
    
    for filepath in eval_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            score = data.get('score', 0)
            old_grade = data.get('short_grade', '?')
            
            # Calculate new grade
            new_grade_info = ranker.calculate_grade(score)
            new_grade = new_grade_info['short_grade']
            
            # Update data
            data['grade'] = new_grade_info['grade']
            data['short_grade'] = new_grade
            data['class'] = new_grade_info['class']
            data['rank_info'] = {
                'percentile': new_grade_info['percentile'],
                'rank': new_grade_info['rank'],
                'total_samples': stats['total_evaluations']
            }
            data['ranking_updated_at'] = datetime.now().isoformat()
            data['version'] = '3.0.0'  # Mark as updated for v3.0
            
            # Track changes
            grade_changes[new_grade] += 1
            
            if old_grade != new_grade and old_grade != '?':
                print(f"  🔄 {os.path.basename(filepath)}: {score}分 {old_grade} → {new_grade}")
            
            # Write updated file
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                updated_count += 1
            else:
                unchanged_count += 1
                
        except Exception as e:
            print(f"  ❌ Error processing {filepath}: {e}")
            error_count += 1
    
    print()
    print("=" * 60)
    print("Recalculation Complete")
    print("=" * 60)
    print(f"✅ Updated: {updated_count} files")
    print(f"⏭️  Dry run: {unchanged_count} files")
    print(f"❌ Errors: {error_count} files")
    print()
    print("New Distribution:")
    for grade, count in grade_changes.items():
        pct = count / len(eval_files) * 100 if eval_files else 0
        print(f"  {grade}: {count} ({pct:.1f}%)")
    print()
    
    if dry_run:
        print("⚠️  This was a dry run. No files were actually modified.")
        print("   Run without --dry-run to apply changes.")
    else:
        print("✅ All files have been updated with new grading system.")


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Recalculate all historical grades using dynamic ranking'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '--history-dir',
        default='data/evaluations',
        help='Directory containing evaluation files'
    )
    
    args = parser.parse_args()
    
    # Change to script directory
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    recalculate_all_grades(
        history_dir=args.history_dir,
        dry_run=args.dry_run
    )
