"""
Semantic Structure scoring dimension.

Evaluates HTML semantic quality, structured data, and content organization.
"""

import json
from typing import Dict, Any, List
from bs4 import BeautifulSoup


class SemanticAnalyzer:
    """Analyzes semantic structure of HTML content."""
    
    # Calibrated thresholds
    MIN_JSONLD_SIZE = 500  # Reduced from 1000 - 500 chars is substantial
    TEXT_DENSITY_THRESHOLD = 0.15  # Reduced from 0.25 - visual sites often have lower density
    
    SEMANTIC_TAGS = ['article', 'nav', 'header', 'main', 'section', 'aside', 'footer']
    
    def analyze(self, soup: BeautifulSoup, snr_percent: float) -> Dict[str, Any]:
        """
        Analyze semantic structure.
        
        Returns dict with score and detailed metrics.
        """
        score = 0
        
        # Semantic tags usage (25 points)
        used_tags = [tag for tag in self.SEMANTIC_TAGS if soup.find(tag)]
        score += (len(used_tags) / len(self.SEMANTIC_TAGS)) * 25
        
        # Heading hierarchy (25 points)
        h1 = soup.find('h1')
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        heading_levels = len(set(h.name for h in headings))
        
        if h1:
            score += 15
        if heading_levels >= 2:
            score += 10
        
        # JSON-LD structured data (25 points)
        json_ld_scripts = soup.find_all('script', {'type': 'application/ld+json'})
        has_json_ld = len(json_ld_scripts) > 0
        json_ld_score = self._analyze_json_ld(json_ld_scripts)
        score += json_ld_score
        
        # Image accessibility (10 points)
        images = soup.find_all('img')
        if images:
            with_alt = len([img for img in images if img.get('alt')])
            score += (with_alt / len(images)) * 10
        
        # Metadata quality (15 points)
        title = soup.find('title')
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if title:
            score += 8
        if meta_desc and meta_desc.get('content'):
            score += 7
        
        # Check for Hidden Gem (visual-rich sites with good structure)
        is_hidden_gem = self._detect_hidden_gem(soup, snr_percent, json_ld_score)
        
        if is_hidden_gem:
            score = max(score, 85)
        
        return {
            'score': min(100, round(score)),
            'semantic_tags_used': used_tags,
            'json_ld_present': has_json_ld,
            'hidden_gem': is_hidden_gem,
            'images_total': len(images),
            'heading_levels': heading_levels,
            'has_h1': bool(h1)
        }
    
    def _analyze_json_ld(self, scripts) -> float:
        """Analyze JSON-LD quality and return score 0-25."""
        if not scripts:
            return 0
        
        total_score = 0
        for script in scripts:
            try:
                content = script.string or ''
                if len(content) > self.MIN_JSONLD_SIZE:
                    data = json.loads(content)
                    # Check for quality indicators
                    quality_points = 0
                    if '@context' in data:
                        quality_points += 5
                    if '@type' in data:
                        quality_points += 5
                    if any(k in data for k in ['name', 'description', 'url']):
                        quality_points += 5
                    if len(content) > 1000:
                        quality_points += 10
                    
                    total_score = max(total_score, quality_points)
            except (json.JSONDecodeError, AttributeError):
                continue
        
        return min(25, total_score)
    
    def _detect_hidden_gem(self, soup: BeautifulSoup, snr: float, json_ld_score: float) -> bool:
        """
        Detect 'Hidden Gem' - visual-rich sites with excellent structured data.
        These sites have low SNR (visual complexity) but provide AI-friendly data.
        """
        text = soup.get_text(strip=True)
        html_str = str(soup)
        
        if not html_str:
            return False
        
        text_density = len(text) / len(html_str)
        
        # Hidden gem criteria:
        # - Low text density (visual-heavy)
        # - Good JSON-LD (score > 15)
        # - Has H1 heading (basic content quality)
        # - SNR < 40% (visual complexity)
        return (
            text_density < self.TEXT_DENSITY_THRESHOLD and
            json_ld_score >= 15 and
            bool(soup.find('h1')) and
            snr < 40
        )
