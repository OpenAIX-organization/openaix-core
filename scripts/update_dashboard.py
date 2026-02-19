#!/usr/bin/env python3
"""
Generate dashboard data from evaluations
Run this after new evaluations are added
"""

import json
import os
from collections import defaultdict

def generate_dashboard_data():
    evaluations = []
    
    # Collect all evaluations
    for root, dirs, files in os.walk('data/evaluations'):
        for f in files:
            if f.endswith('.json') and not f.startswith('evaluated'):
                try:
                    with open(os.path.join(root, f), 'r') as fp:
                        data = json.load(fp)
                        if isinstance(data, dict) and 'score' in data:
                            eval_summary = {
                                'url': data.get('target', ''),
                                'domain': data.get('target', '').replace('https://', '').replace('http://', '').replace('www.', ''),
                                'score': data.get('score', 0),
                                'grade': data.get('grade', ''),
                                'short_grade': data.get('short_grade', ''),
                                'class': data.get('class', ''),
                                'site_type': data.get('site_type', {}).get('type', 'unknown'),
                                'site_description': data.get('site_type', {}).get('description', ''),
                                'percentile': data.get('rank_info', {}).get('percentile', ''),
                                'rank': data.get('rank_info', {}).get('rank', ''),
                                'metrics': {
                                    'snr': data.get('metrics', {}).get('snr', ''),
                                    'token_cost': data.get('metrics', {}).get('token_cost', ''),
                                    'json_ld': data.get('metrics', {}).get('json_ld', False),
                                    'llms_txt': data.get('metrics', {}).get('llms_txt', False),
                                    'api_features': data.get('metrics', {}).get('api_features', []),
                                },
                                'dimensions': {
                                    'snr': data.get('dimensions', {}).get('snr', {}).get('score', 0),
                                    'semantic': data.get('dimensions', {}).get('semantic', {}).get('score', 0),
                                    'token_economy': data.get('dimensions', {}).get('token_economy', {}).get('score', 0),
                                    'permissions': data.get('dimensions', {}).get('permissions', {}).get('score', 0),
                                    'api': data.get('dimensions', {}).get('api_availability', {}).get('score', 0),
                                },
                                'suggestions': data.get('suggestions', [])[:3],
                                'timestamp': data.get('timestamp', ''),
                                'version': data.get('version', '')
                            }
                            evaluations.append(eval_summary)
                except Exception as e:
                    pass
    
    # Sort by score descending
    evaluations.sort(key=lambda x: x['score'], reverse=True)
    
    # Calculate statistics
    total = len(evaluations)
    grade_counts = defaultdict(int)
    for e in evaluations:
        grade_counts[e['short_grade']] += 1
    
    stats = {
        'total_evaluations': total,
        'grade_distribution': dict(grade_counts),
        'average_score': round(sum(e['score'] for e in evaluations) / total, 1) if total else 0,
        'last_updated': evaluations[0]['timestamp'] if evaluations else '',
        'thresholds': {
            'S': 75,
            'A': 63,
            'B': 52
        }
    }
    
    # Save aggregated data
    output = {
        'statistics': stats,
        'evaluations': evaluations
    }
    
    os.makedirs('web/dashboard/data', exist_ok=True)
    with open('web/dashboard/data/evaluations.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f'✅ Generated dashboard data: {total} evaluations')
    print(f'📊 Grade distribution: {dict(grade_counts)}')
    print(f'📁 Saved to: web/dashboard/data/evaluations.json')

if __name__ == '__main__':
    generate_dashboard_data()
