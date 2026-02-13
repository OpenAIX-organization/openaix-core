"""
Main OpenAIX Scorer - orchestrates all scoring dimensions.
"""

import logging
from typing import Dict, Any, List
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

from .dimensions import SNRAnalyzer, SemanticAnalyzer, TokenEconomyAnalyzer, PermissionsAnalyzer
from .utils import normalize_url, get_timestamp

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger('openaix')


class OpenAIXScorer:
    """Evaluates AI Experience (AIX) of websites."""
    
    WEIGHTS = {
        'snr': 0.30,
        'semantic': 0.30,
        'token_economy': 0.20,
        'permissions': 0.20,
    }
    
    THRESHOLDS = {
        'silicon_native': 85,
        'agent_friendly': 70,
        'human_optimized': 50,
    }
    
    def __init__(self, timeout: int = 10, rate_limit: float = 1.0):
        self.timeout = timeout
        self.rate_limit = rate_limit
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        # Initialize analyzers
        self.snr_analyzer = SNRAnalyzer()
        self.semantic_analyzer = SemanticAnalyzer()
        self.token_analyzer = TokenEconomyAnalyzer()
        self.permissions_analyzer = PermissionsAnalyzer(self.session, timeout)
    
    def score(self, url: str) -> Dict[str, Any]:
        """Score a website and return complete report."""
        url = normalize_url(url)
        print(f"🔍 Evaluating AIX: {url}")
        
        try:
            response = self.session.get(url, timeout=self.timeout)
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
        except Exception as e:
            return self._error_response(url, str(e))
        
        # Analyze each dimension
        print("  📊 Analyzing Signal-to-Noise Ratio...")
        snr_result = self.snr_analyzer.analyze(html)
        
        print("  🏗️  Evaluating Semantic Structure...")
        semantic_result = self.semantic_analyzer.analyze(soup, snr_result['snr_percent'])
        
        print("  💰 Calculating Token Economy...")
        token_result = self.token_analyzer.analyze(snr_result['clean_tokens'])
        
        print("  🔐 Checking Agent Permissions...")
        permissions_result = self.permissions_analyzer.analyze(url)
        
        # Aggregate scores
        dimensions = {
            'snr': snr_result,
            'semantic': semantic_result,
            'token_economy': token_result,
            'permissions': permissions_result
        }
        
        total_score = round(sum(
            dim['score'] * self.WEIGHTS[dim_name]
            for dim_name, dim in dimensions.items()
        ))
        
        grade_info = self._calculate_grade(total_score)
        
        return {
            'target': url,
            'score': total_score,
            'grade': grade_info['grade'],
            'class': grade_info['class'],
            'metrics': {
                'snr': f"{snr_result['snr_percent']:.0f}%",
                'token_cost': token_result['cost_rating'],
                'json_ld': semantic_result['json_ld_present'],
                'llms_txt': permissions_result['llms_txt_present']
            },
            'dimensions': dimensions,
            'suggestions': self._generate_suggestions(dimensions, total_score),
            'timestamp': get_timestamp(),
            'version': '2.0.0'
        }
    
    def _calculate_grade(self, score: int) -> Dict[str, str]:
        """Calculate letter grade from score."""
        if score >= self.THRESHOLDS['silicon_native']:
            return {'grade': 'Class S (Silicon Native)', 'class': 'Silicon Native'}
        elif score >= self.THRESHOLDS['agent_friendly']:
            return {'grade': 'Class A (Agent Friendly)', 'class': 'Agent Friendly'}
        elif score >= self.THRESHOLDS['human_optimized']:
            return {'grade': 'Class B (Human Optimized)', 'class': 'Human Optimized'}
        else:
            return {'grade': 'Class C (Needs Improvement)', 'class': 'Needs Improvement'}
    
    def _generate_suggestions(self, dimensions: Dict, total_score: int) -> List[str]:
        """Generate improvement suggestions based on results."""
        suggestions = []
        
        if total_score >= 85:
            suggestions.append("✨ Silicon Native! Excellent for AI agents.")
            if not dimensions['permissions']['llms_txt_present']:
                suggestions.append("💡 Consider adding /llms.txt for future-proofing.")
        elif total_score >= 70:
            suggestions.append("✅ Agent Friendly. Good structure and low noise.")
        elif total_score >= 50:
            suggestions.append("⚠️ Acceptable but needs improvement.")
            if dimensions['snr']['snr_percent'] < 20:
                suggestions.append("📉 Low SNR: Consider reducing HTML boilerplate.")
            if dimensions['token_economy']['cost_rating'] in ['High', 'Very High']:
                suggestions.append("💰 High token cost: Consider content summarization.")
        else:
            suggestions.append("🔧 Needs significant improvements.")
            if dimensions['permissions']['http_status'] in [401, 403]:
                suggestions.append("🔒 Access blocked: Check robots.txt or authentication.")
            elif dimensions['snr']['snr_percent'] < 10:
                suggestions.append("🏗️  Add JSON-LD structured data for better AI understanding.")
        
        if total_score < 85 and not dimensions['semantic']['json_ld_present']:
            suggestions.append("📋 Add JSON-LD structured data to improve AI comprehension.")
        
        return suggestions
    
    def _error_response(self, url: str, error_message: str) -> Dict[str, Any]:
        """Generate error response."""
        return {
            'target': url,
            'score': 0,
            'grade': 'Error',
            'class': 'Error',
            'error': error_message,
            'suggestions': ['❌ Failed to evaluate. Check URL and try again.'],
            'timestamp': get_timestamp(),
            'version': '2.0.0'
        }
