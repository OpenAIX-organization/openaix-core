"""
Dynamic Ranking System for OpenAIX v3.0
Grades based on percentile ranking, not absolute scores
"""

import json
import os
from typing import Dict, List, Optional
from datetime import datetime


class DynamicRanker:
    """Calculate grades based on historical score distribution"""
    
    # Percentile thresholds (customizable)
    PERCENTILES = {
        'S': 0.98,  # Top 2%
        'A': 0.80,  # Top 20% (includes S)
        'B': 0.50,  # Top 50% (includes A and S)
    }
    
    def __init__(self, history_dir: str = 'data/evaluations'):
        self.history_dir = history_dir
        self._scores_cache = None
        self._cache_timestamp = None
    
    def load_all_scores(self, exclude_current: Optional[str] = None) -> List[int]:
        """Load all historical scores from evaluation files"""
        scores = []
        for root, dirs, files in os.walk(self.history_dir):
            for f in files:
                if f.endswith('.json'):
                    filepath = os.path.join(root, f)
                    # Optionally exclude current file being processed
                    if exclude_current and filepath == exclude_current:
                        continue
                    try:
                        with open(filepath, 'r', encoding='utf-8') as fp:
                            data = json.load(fp)
                            # Handle both dict and list formats
                            if isinstance(data, dict):
                                score = data.get('score', 0)
                            elif isinstance(data, list) and len(data) > 0:
                                score = data[0].get('score', 0) if isinstance(data[0], dict) else 0
                            else:
                                score = 0
                            if score > 0:
                                scores.append(score)
                    except (json.JSONDecodeError, IOError, AttributeError):
                        continue
        return sorted(scores)
    
    def get_percentile_thresholds(self, scores: Optional[List[int]] = None) -> Dict:
        """Calculate percentile-based thresholds"""
        if scores is None:
            scores = self.load_all_scores()
        
        if not scores:
            # Fallback to fixed thresholds if no history
            return {
                'S': 75,
                'A': 60,
                'B': 45,
                'total_samples': 0,
                'updated_at': datetime.now().isoformat(),
                'is_fallback': True
            }
        
        n = len(scores)
        
        # Calculate thresholds at percentiles
        p98_idx = min(int(n * (1 - self.PERCENTILES['S'])), n - 1)
        p80_idx = min(int(n * (1 - self.PERCENTILES['A'])), n - 1)
        p50_idx = min(int(n * (1 - self.PERCENTILES['B'])), n - 1)
        
        return {
            'S': scores[p98_idx] if n > 0 else 75,
            'A': scores[p80_idx] if n > 0 else 60,
            'B': scores[p50_idx] if n > 0 else 45,
            'total_samples': n,
            'updated_at': datetime.now().isoformat(),
            'is_fallback': False,
            'distribution': {
                'min': scores[0] if scores else 0,
                'max': scores[-1] if scores else 100,
                'median': scores[n // 2] if scores else 50,
                'p90': scores[int(n * 0.90)] if n > 10 else 70,
            }
        }
    
    def calculate_grade(self, score: int, thresholds: Optional[Dict] = None) -> Dict[str, str]:
        """Calculate grade based on dynamic thresholds"""
        if thresholds is None:
            thresholds = self.get_percentile_thresholds()
        
        s_threshold = thresholds['S']
        a_threshold = thresholds['A']
        b_threshold = thresholds['B']
        total = thresholds.get('total_samples', 0)
        
        if score >= s_threshold:
            return {
                'grade': 'Class S (Silicon Native)',
                'short_grade': 'S',
                'class': 'Silicon Native',
                'percentile': '>98%',
                'rank': f'Top 2%',
                'description': 'Top-tier AI experience'
            }
        elif score >= a_threshold:
            return {
                'grade': 'Class A (Agent Friendly)',
                'short_grade': 'A',
                'class': 'Agent Friendly',
                'percentile': '80%-98%',
                'rank': f'Top 20%',
                'description': 'Excellent for AI agents'
            }
        elif score >= b_threshold:
            return {
                'grade': 'Class B (Human Optimized)',
                'short_grade': 'B',
                'class': 'Human Optimized',
                'percentile': '50%-80%',
                'rank': f'Top 50%',
                'description': 'Good with room for improvement'
            }
        else:
            return {
                'grade': 'Class C (Needs Improvement)',
                'short_grade': 'C',
                'class': 'Needs Improvement',
                'percentile': '<50%',
                'rank': f'Bottom 50%',
                'description': 'Significant improvements needed'
            }
    
    def get_statistics(self) -> Dict:
        """Get current ranking statistics"""
        scores = self.load_all_scores()
        thresholds = self.get_percentile_thresholds(scores)
        
        if not scores:
            return {
                'total_evaluations': 0,
                'thresholds': thresholds,
                'distribution': {}
            }
        
        s_threshold = thresholds['S']
        a_threshold = thresholds['A']
        b_threshold = thresholds['B']
        
        # Count distribution
        s_count = sum(1 for s in scores if s >= s_threshold)
        a_count = sum(1 for s in scores if a_threshold <= s < s_threshold)
        b_count = sum(1 for s in scores if b_threshold <= s < a_threshold)
        c_count = sum(1 for s in scores if s < b_threshold)
        
        n = len(scores)
        
        return {
            'total_evaluations': n,
            'thresholds': thresholds,
            'distribution': {
                'S': {
                    'count': s_count,
                    'percent': f'{s_count/n*100:.1f}%',
                    'threshold': f'≥{s_threshold}'
                },
                'A': {
                    'count': a_count,
                    'percent': f'{a_count/n*100:.1f}%',
                    'threshold': f'{a_threshold}-{s_threshold-1}'
                },
                'B': {
                    'count': b_count,
                    'percent': f'{b_count/n*100:.1f}%',
                    'threshold': f'{b_threshold}-{a_threshold-1}'
                },
                'C': {
                    'count': c_count,
                    'percent': f'{c_count/n*100:.1f}%',
                    'threshold': f'<{b_threshold}'
                },
            },
            'updated_at': datetime.now().isoformat()
        }
    
    def format_ranking_info(self, score: int) -> str:
        """Format ranking info for display"""
        grade_info = self.calculate_grade(score)
        stats = self.get_statistics()
        
        lines = [
            f"Score: {score}/100",
            f"Grade: {grade_info['grade']}",
            f"Ranking: {grade_info['rank']} ({grade_info['percentile']})",
            f"Total evaluated: {stats['total_evaluations']} sites"
        ]
        
        return '\n'.join(lines)


# Convenience functions for direct usage
def get_current_thresholds(history_dir: str = 'data/evaluations') -> Dict:
    """Get current dynamic thresholds"""
    ranker = DynamicRanker(history_dir)
    return ranker.get_percentile_thresholds()


def calculate_dynamic_grade(score: int, history_dir: str = 'data/evaluations') -> Dict[str, str]:
    """Calculate grade using dynamic ranking"""
    ranker = DynamicRanker(history_dir)
    return ranker.calculate_grade(score)


def get_ranking_statistics(history_dir: str = 'data/evaluations') -> Dict:
    """Get current ranking statistics"""
    ranker = DynamicRanker(history_dir)
    return ranker.get_statistics()
