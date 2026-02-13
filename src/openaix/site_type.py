"""
Site type detection for dynamic weight adjustment.

Automatically classifies websites into 4 types:
- documentation: High SNR, clear structure
- product: Visual-rich, needs Hidden Gem compensation
- platform: API-first, CLI tools, multi-page
- content: Text-heavy, narrative
"""

from typing import Dict, Any
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class SiteTypeDetector:
    """Detects website type for applying appropriate scoring weights."""
    
    INDICATORS = {
        'documentation': {
            'paths': ['/docs', '/documentation', '/reference', '/guide', 
                     '/tutorial', '/api-docs', '/help', '/manual'],
            'keywords': ['documentation', 'reference', 'guide', 'tutorial',
                        'getting started', 'quickstart', 'handbook'],
            'schema_types': ['TechArticle', 'APIReference', 'Documentation']
        },
        'product': {
            'paths': ['/product', '/pricing', '/features', '/solutions',
                     '/enterprise', '/demo', '/buy', '/shop'],
            'keywords': ['pricing', 'features', 'solutions', 'product',
                        'buy now', 'get started', 'free trial', 'enterprise'],
            'schema_types': ['Product', 'Service', 'Organization']
        },
        'platform': {
            'paths': ['/api', '/developers', '/dashboard', '/console',
                     '/app', '/platform', '/integrations', '/webhooks'],
            'keywords': ['api', 'developers', 'dashboard', 'platform',
                        'integrate', 'sdk', 'cli', 'automation'],
            'schema_types': ['WebAPI', 'SoftwareApplication']
        },
        'content': {
            'paths': ['/blog', '/article', '/news', '/post',
                     '/story', '/journal', '/magazine'],
            'keywords': ['blog', 'article', 'news', 'post', 'story',
                        'written by', 'published', 'reading time'],
            'schema_types': ['BlogPosting', 'NewsArticle', 'Article']
        }
    }
    
    def detect(self, url: str, html: str) -> Dict[str, Any]:
        """
        Detect site type using multiple signals.
        
        Returns:
            Dict with site_type, confidence_score, and signals_detected
        """
        scores = {
            'documentation': 0,
            'product': 0,
            'platform': 0,
            'content': 0
        }
        signals = []
        
        # Parse URL
        parsed = urlparse(url)
        path = parsed.path.lower()
        domain = parsed.netloc.lower()
        
        # Signal 1: URL path patterns (40% weight)
        for site_type, indicators in self.INDICATORS.items():
            for indicator_path in indicators['paths']:
                if indicator_path in path:
                    scores[site_type] += 40
                    signals.append(f"path:{indicator_path}")
        
        # Signal 2: API subdomain (strong signal for platform)
        if 'api.' in domain or domain.startswith('api.'):
            scores['platform'] += 60
            signals.append("api_subdomain")
        
        # Signal 3: HTML content analysis (35% weight)
        soup = BeautifulSoup(html, 'lxml')
        text = soup.get_text().lower()
        
        for site_type, indicators in self.INDICATORS.items():
            for keyword in indicators['keywords']:
                if keyword in text:
                    scores[site_type] += 35
                    signals.append(f"keyword:{keyword}")
                    break
        
        # Signal 4: JSON-LD schema types (15% weight)
        json_ld_scripts = soup.find_all('script', {'type': 'application/ld+json'})
        for script in json_ld_scripts:
            try:
                import json
                data = json.loads(script.string or '{}')
                schema_type = data.get('@type', '')
                
                for site_type, indicators in self.INDICATORS.items():
                    if schema_type in indicators['schema_types']:
                        scores[site_type] += 15
                        signals.append(f"schema:{schema_type}")
            except:
                continue
        
        # Signal 5: Special platform indicators
        if self._has_platform_indicators(html, domain):
            scores['platform'] += 25
            signals.append("platform_indicators")
        
        # Determine winner
        detected_type = max(scores, key=scores.get)
        confidence = scores[detected_type]
        total_score = sum(scores.values())
        
        # Normalize confidence to 0-100
        confidence_pct = min(100, int((confidence / total_score) * 100)) if total_score > 0 else 0
        
        return {
            'site_type': detected_type,
            'confidence': confidence_pct,
            'scores': scores,
            'signals': list(set(signals))  # Remove duplicates
        }
    
    def _has_platform_indicators(self, html: str, domain: str) -> bool:
        """Check for strong platform indicators."""
        indicators = [
            'github.com',
            'vercel.com',
            'netlify.com',
            'stripe.com',
            'openai.com',
            'linear.app',
            'console.',
            'dashboard.',
            'developers.',
            '/graphql',
            '/webhook',
            '/oauth',
            '/token',
            'api key',
            'api token',
            'access token'
        ]
        
        html_lower = html.lower()
        combined = f"{domain} {html_lower}"
        
        return any(indicator in combined for indicator in indicators)
