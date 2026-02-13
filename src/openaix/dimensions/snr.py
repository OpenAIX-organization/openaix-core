"""
Signal-to-Noise Ratio (SNR) scoring dimension.

Measures the density of semantic content vs HTML boilerplate.
"""

from typing import Dict, Any
import tiktoken
from bs4 import BeautifulSoup
from markdownify import markdownify as md


class SNRAnalyzer:
    """Analyzes Signal-to-Noise Ratio of HTML content."""
    
    # Calibrated thresholds based on real-world data
    THRESHOLD_EXCELLENT = 40  # 40%+ SNR is excellent
    THRESHOLD_GOOD = 20       # 20-40% is good
    THRESHOLD_ACCEPTABLE = 10 # 10-20% is acceptable
    THRESHOLD_POOR = 5        # 5-10% needs improvement
    
    def __init__(self):
        self.tokenizer = tiktoken.get_encoding("cl100k_base")
    
    def analyze(self, html: str) -> Dict[str, Any]:
        """
        Analyze SNR of HTML content.
        
        Returns dict with:
        - score: 0-100
        - snr_percent: SNR percentage
        - raw_tokens: token count of raw HTML
        - clean_tokens: token count of cleaned content
        """
        raw_tokens = len(self.tokenizer.encode(html))
        soup = BeautifulSoup(html, 'lxml')
        
        # Remove non-content elements
        for element in soup([
            'script', 'style', 'noscript', 'iframe', 'canvas', 
            'svg', 'template', 'embed', 'object'
        ]):
            element.decompose()
        
        clean_html = str(soup)
        markdown_content = md(clean_html)
        clean_tokens = len(self.tokenizer.encode(markdown_content))
        
        snr = (clean_tokens / raw_tokens * 100) if raw_tokens > 0 else 0
        score = self._calculate_score(snr)
        
        return {
            'score': round(score),
            'snr_percent': round(snr, 2),
            'raw_tokens': raw_tokens,
            'clean_tokens': clean_tokens
        }
    
    def _calculate_score(self, snr: float) -> float:
        """Calculate score from SNR percentage with smooth curve."""
        if snr >= self.THRESHOLD_EXCELLENT:
            return 100
        elif snr >= self.THRESHOLD_GOOD:
            # Smooth curve from 20% to 40%
            return 70 + ((snr - self.THRESHOLD_GOOD) / (self.THRESHOLD_EXCELLENT - self.THRESHOLD_GOOD)) * 30
        elif snr >= self.THRESHOLD_ACCEPTABLE:
            # Smooth curve from 10% to 20%
            return 50 + ((snr - self.THRESHOLD_ACCEPTABLE) / (self.THRESHOLD_GOOD - self.THRESHOLD_ACCEPTABLE)) * 20
        elif snr >= self.THRESHOLD_POOR:
            # Smooth curve from 5% to 10%
            return 30 + ((snr - self.THRESHOLD_POOR) / (self.THRESHOLD_ACCEPTABLE - self.THRESHOLD_POOR)) * 20
        else:
            # Below 5%
            return max(0, snr * 6)
