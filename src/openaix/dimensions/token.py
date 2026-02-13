"""
Token Economy scoring dimension.

Calculates the cost for an LLM to read the page content.
"""

from typing import Dict, Any


class TokenEconomyAnalyzer:
    """Analyzes token economy and cost efficiency."""
    
    # Calibrated thresholds (more lenient)
    THRESHOLD_LOW = 2000      # <2k tokens = excellent (was 1000)
    THRESHOLD_MEDIUM = 6000   # 2-6k = good (was 3000)
    THRESHOLD_HIGH = 15000    # 6-15k = acceptable (was 8000)
    
    # Cost per 1k tokens (GPT-4 pricing as reference)
    COST_PER_1K_TOKENS = 0.03
    
    def analyze(self, clean_tokens: int) -> Dict[str, Any]:
        """
        Analyze token economy.
        
        Args:
            clean_tokens: Number of content tokens (after cleaning)
            
        Returns:
            Dict with score, cost rating, and estimated cost
        """
        if clean_tokens < self.THRESHOLD_LOW:
            cost_rating, score = "Low", 100
        elif clean_tokens < self.THRESHOLD_MEDIUM:
            cost_rating, score = "Medium", 85
        elif clean_tokens < self.THRESHOLD_HIGH:
            cost_rating, score = "High", 65
        else:
            cost_rating, score = "Very High", 40
        
        estimated_cost = (clean_tokens / 1000) * self.COST_PER_1K_TOKENS
        
        return {
            'score': score,
            'cost_rating': cost_rating,
            'clean_tokens': clean_tokens,
            'estimated_cost_usd': round(estimated_cost, 4)
        }
