"""
Main OpenAIX Scorer v2.1 - with API Availability and Dynamic Weights
"""

import logging
from typing import Dict, Any, List
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

from .dimensions import (
    SNRAnalyzer, SemanticAnalyzer, TokenEconomyAnalyzer, 
    PermissionsAnalyzer, APIAvailabilityAnalyzer
)
from .site_type import SiteTypeDetector
from .weights import get_weights, get_site_description
from .utils import normalize_url, get_timestamp
from .dynamic_ranking import DynamicRanker

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger('openaix')


class OpenAIXScorer:
    """Evaluates AI Experience (AIX) of websites with dynamic weights and ranking."""
    
    def __init__(self, timeout: int = 10, rate_limit: float = 1.0, 
                 multi_page: bool = True, history_dir: str = 'data/evaluations'):
        self.timeout = timeout
        self.rate_limit = rate_limit
        self.multi_page = multi_page
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        self.snr_analyzer = SNRAnalyzer()
        self.semantic_analyzer = SemanticAnalyzer()
        self.token_analyzer = TokenEconomyAnalyzer()
        self.permissions_analyzer = PermissionsAnalyzer(self.session, timeout)
        self.api_analyzer = APIAvailabilityAnalyzer(timeout)
        self.site_detector = SiteTypeDetector()
        self.ranker = DynamicRanker(history_dir)
    
    def score(self, url: str) -> Dict[str, Any]:
        """Score a website with multi-page sampling and dynamic weights."""
        url = normalize_url(url)
        print(f"🔍 Evaluating AIX: {url}")
        
        try:
            # Fetch homepage for site type detection
            response = self.session.get(url, timeout=self.timeout)
            homepage_html = response.text
        except Exception as e:
            return self._error_response(url, str(e))
        
        # Detect site type
        print("  🔎 Detecting site type...")
        site_type_result = self.site_detector.detect(url, homepage_html)
        site_type = site_type_result['site_type']
        weights = get_weights(site_type)
        
        print(f"     Detected: {site_type} (confidence: {site_type_result['confidence']}%)")
        print(f"     Using weights: API={weights['api_availability']*100:.0f}%, SNR={weights['snr']*100:.0f}%")
        
        # Determine pages to test
        if self.multi_page:
            pages = self._get_pages_to_test(url, site_type)
        else:
            pages = [url]
        
        print(f"  📄 Testing {len(pages)} page(s)...")
        
        # Score each page
        page_results = []
        for page_url in pages:
            result = self._score_single_page(page_url, weights, page_url == url)
            page_results.append(result)
            print(f"     {page_url}: {result['score']}/100")
        
        # Calculate final score with multi-page weighting
        final_score = self._aggregate_scores(page_results)
        grade_info = self._calculate_grade(final_score)
        
        # Use homepage for API analysis (site-level)
        print("  🔌 Analyzing API availability...")
        api_result = self.api_analyzer.analyze(url, homepage_html)
        
        # Combine all dimensions from first page + API
        dimensions = page_results[0]['dimensions'].copy()
        dimensions['api_availability'] = api_result
        
        # Recalculate final score with API
        weighted_sum = (
            dimensions['snr']['score'] * weights['snr'] +
            dimensions['semantic']['score'] * weights['semantic'] +
            dimensions['token_economy']['score'] * weights['token_economy'] +
            dimensions['permissions']['score'] * weights['permissions'] +
            api_result['score'] * weights['api_availability']
        )
        final_score = round(weighted_sum)
        
        return {
            'target': url,
            'score': final_score,
            'grade': grade_info['grade'],
            'class': grade_info['class'],
            'rank_info': {
                'percentile': grade_info.get('percentile', 'N/A'),
                'rank': grade_info.get('rank', 'N/A'),
                'total_samples': self.ranker.get_percentile_thresholds().get('total_samples', 0)
            },
            'site_type': {
                'type': site_type,
                'description': get_site_description(site_type),
                'confidence': site_type_result['confidence'],
                'signals': site_type_result['signals']
            },
            'weights_used': {k: round(v, 2) for k, v in weights.items()},
            'pages_tested': len(pages),
            'page_scores': [{'url': r['url'], 'score': r['score']} for r in page_results],
            'metrics': {
                'snr': f"{dimensions['snr']['snr_percent']:.0f}%",
                'token_cost': dimensions['token_economy']['cost_rating'],
                'json_ld': dimensions['semantic']['json_ld_present'],
                'llms_txt': dimensions['permissions']['llms_txt_present'],
                'api_features': api_result['features'],
                'api_endpoints': len(api_result.get('endpoints_found', []))
            },
            'dimensions': dimensions,
            'suggestions': self._generate_suggestions(dimensions, final_score, site_type),
            'timestamp': get_timestamp(),
            'version': '2.1.0'
        }
    
    def _score_single_page(self, url: str, weights: Dict[str, float], 
                          is_homepage: bool) -> Dict[str, Any]:
        """Score a single page."""
        try:
            response = self.session.get(url, timeout=self.timeout)
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
        except Exception as e:
            return {
                'url': url,
                'score': 0,
                'error': str(e),
                'dimensions': {}
            }
        
        # Analyze dimensions
        snr_result = self.snr_analyzer.analyze(html)
        semantic_result = self.semantic_analyzer.analyze(soup, snr_result['snr_percent'])
        token_result = self.token_analyzer.analyze(snr_result['clean_tokens'])
        permissions_result = self.permissions_analyzer.analyze(url)
        
        dimensions = {
            'snr': snr_result,
            'semantic': semantic_result,
            'token_economy': token_result,
            'permissions': permissions_result
        }
        
        # Calculate weighted score (without API for single page)
        weighted_sum = (
            snr_result['score'] * weights['snr'] +
            semantic_result['score'] * weights['semantic'] +
            token_result['score'] * weights['token_economy'] +
            permissions_result['score'] * weights['permissions']
        )
        
        # Normalize to account for missing API weight on non-homepage
        if not is_homepage:
            available_weight = (weights['snr'] + weights['semantic'] + 
                              weights['token_economy'] + weights['permissions'])
            weighted_sum = weighted_sum / available_weight * sum([
                weights['snr'], weights['semantic'], 
                weights['token_economy'], weights['permissions']
            ])
        
        return {
            'url': url,
            'score': round(weighted_sum),
            'dimensions': dimensions
        }
    
    def _get_pages_to_test(self, base_url: str, site_type: str) -> List[str]:
        """Get representative pages to test based on site type."""
        pages = [base_url]
        
        candidates = {
            'documentation': ['/docs', '/guide', '/tutorial', '/reference'],
            'product': ['/features', '/pricing', '/about', '/solutions'],
            'platform': ['/docs', '/api', '/developers', '/features'],
            'content': ['/blog', '/articles', '/posts', '/about'],
            'default': ['/about', '/docs', '/help']
        }
        
        paths = candidates.get(site_type, candidates['default'])
        
        for path in paths[:2]:  # Try up to 2 additional pages
            test_url = f"{base_url.rstrip('/')}{path}"
            try:
                response = self.session.get(test_url, timeout=self.timeout)
                if response.status_code == 200 and len(response.text) > 1000:
                    pages.append(test_url)
                    if len(pages) >= 3:
                        break
            except:
                continue
        
        return pages
    
    def _aggregate_scores(self, page_results: List[Dict]) -> int:
        """Aggregate multi-page scores with homepage weighted higher."""
        if len(page_results) == 1:
            return page_results[0]['score']
        elif len(page_results) == 2:
            return round(page_results[0]['score'] * 0.6 + page_results[1]['score'] * 0.4)
        else:
            return round(
                page_results[0]['score'] * 0.5 +
                page_results[1]['score'] * 0.25 +
                page_results[2]['score'] * 0.25
            )
    
    def _calculate_grade(self, score: int) -> Dict[str, str]:
        """Calculate grade using dynamic percentile ranking."""
        return self.ranker.calculate_grade(score)
    
    def _generate_suggestions(self, dimensions: Dict, total_score: int, 
                             site_type: str) -> List[str]:
        """Generate improvement suggestions based on dynamic grade."""
        suggestions = []
        
        # Get dynamic grade info
        grade_info = self._calculate_grade(total_score)
        short_grade = grade_info.get('short_grade', 'C')
        
        if short_grade == 'S':
            suggestions.append("✨ Class S - Silicon Native! Top 2% AI experience.")
        elif short_grade == 'A':
            suggestions.append("✅ Class A - Agent Friendly. Top 20% performance.")
        elif short_grade == 'B':
            suggestions.append("⚠️ Class B - Human Optimized. Top 50%, room to improve.")
        else:
            suggestions.append("🔧 Class C - Needs Improvement. Bottom 50%.")
        
        # Dimension-specific suggestions
        if dimensions['snr']['score'] < 30:
            suggestions.append("📉 Low SNR: Consider SSR or reducing JS dependencies.")
        
        if not dimensions['semantic']['json_ld_present']:
            suggestions.append("📋 Add JSON-LD structured data for better AI understanding.")
        
        if not dimensions['permissions']['llms_txt_present']:
            suggestions.append("📝 Add /llms.txt to describe your site for AI agents.")
        
        # API-specific for platform sites
        if site_type == 'platform' and dimensions['api_availability']['score'] < 50:
            suggestions.append("🔌 As a platform, consider adding OpenAPI spec or API documentation.")
        
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
            'version': '2.1.0'
        }
