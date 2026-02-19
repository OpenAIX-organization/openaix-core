#!/usr/bin/env python3
"""
Quick recalculation of grades using dynamic ranking - batch processing
"""

import json
import os
import glob
from collections import defaultdict

# Step 1: Collect all scores
print("📊 Step 1: Collecting all scores...")
scores = []
for root, dirs, files in os.walk('data/evaluations'):
    for f in files:
        if f.endswith('.json'):
            try:
                with open(os.path.join(root, f)) as fp:
                    data = json.load(fp)
                    if isinstance(data, dict):
                        score = data.get('score', 0)
                        if score > 0:
                            scores.append(score)
            except:
                pass

print(f"   Found {len(scores)} valid scores")

# Step 2: Calculate thresholds
print("\n📈 Step 2: Calculating percentile thresholds...")
sorted_scores = sorted(scores)
n = len(sorted_scores)

p98 = sorted_scores[int(n * 0.98)]
p80 = sorted_scores[int(n * 0.80)]
p50 = sorted_scores[int(n * 0.50)]

print(f"   S (top 2%): ≥{p98}")
print(f"   A (top 20%): {p80}-{p98-1}")
print(f"   B (top 50%): {p50}-{p80-1}")
print(f"   C (bottom 50%): <{p50}")

# Step 3: Count distribution
s_count = sum(1 for s in scores if s >= p98)
a_count = sum(1 for s in scores if p80 <= s < p98)
b_count = sum(1 for s in scores if p50 <= s < p80)
c_count = sum(1 for s in scores if s < p50)

print(f"\n📊 Distribution:")
print(f"   S: {s_count} ({s_count/n*100:.1f}%)")
print(f"   A: {a_count} ({a_count/n*100:.1f}%)")
print(f"   B: {b_count} ({b_count/n*100:.1f}%)")
print(f"   C: {c_count} ({c_count/n*100:.1f}%)")

# Step 4: Update all files
print(f"\n📝 Step 3: Updating {len(glob.glob('data/evaluations/**/*.json', recursive=True))} files...")

updated = 0
errors = 0

for root, dirs, files in os.walk('data/evaluations'):
    for f in files:
        if f.endswith('.json'):
            filepath = os.path.join(root, f)
            try:
                with open(filepath, 'r') as fp:
                    data = json.load(fp)
                
                if not isinstance(data, dict):
                    continue
                    
                score = data.get('score', 0)
                if score == 0:
                    continue
                
                # Calculate new grade
                if score >= p98:
                    grade = 'Class S (Silicon Native)'
                    short = 'S'
                    cls = 'Silicon Native'
                    pct = '>98%'
                    rank = 'Top 2%'
                elif score >= p80:
                    grade = 'Class A (Agent Friendly)'
                    short = 'A'
                    cls = 'Agent Friendly'
                    pct = '80%-98%'
                    rank = 'Top 20%'
                elif score >= p50:
                    grade = 'Class B (Human Optimized)'
                    short = 'B'
                    cls = 'Human Optimized'
                    pct = '50%-80%'
                    rank = 'Top 50%'
                else:
                    grade = 'Class C (Needs Improvement)'
                    short = 'C'
                    cls = 'Needs Improvement'
                    pct = '<50%'
                    rank = 'Bottom 50%'
                
                # Update data
                data['grade'] = grade
                data['short_grade'] = short
                data['class'] = cls
                data['rank_info'] = {
                    'percentile': pct,
                    'rank': rank,
                    'total_samples': n,
                    'thresholds': {'S': p98, 'A': p80, 'B': p50}
                }
                data['version'] = '3.0.0'
                
                with open(filepath, 'w') as fp:
                    json.dump(data, fp, indent=2)
                
                updated += 1
                if updated % 500 == 0:
                    print(f"   ... updated {updated} files")
                    
            except Exception as e:
                errors += 1

print(f"\n✅ Complete!")
print(f"   Updated: {updated} files")
print(f"   Errors: {errors} files")
