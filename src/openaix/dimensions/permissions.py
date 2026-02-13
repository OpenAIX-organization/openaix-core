"""
Agent Permissions scoring dimension.

Verifies robots.txt, response accessibility, and AI-specific files.
"""

import time
from typing import Dict, Any, List
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
import requests


class PermissionsAnalyzer:
    """Analyzes accessibility and permissions for AI agents."""
    
    # AI agents to check
    AI_AGENTS = [
        'GPTBot', 'CCBot', 'anthropic-ai', 'ClaudeBot', 
        'ChatGPT-User', 'Google-Extended', 'PerplexityBot'
    ]
    
    # Calibrated thresholds
    SLOW_RESPONSE_MS = 3000  # Increased from 2000ms
    
    def __init__(self, session: requests.Session, timeout: int = 10):
        self.session = session
        self.timeout = timeout
        self.last_request_time = 0
        self.rate_limit = 1.0  # seconds between requests
    
    def _rate_limited_request(self, url: str, **kwargs):
        """Make rate-limited request."""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit:
            time.sleep(self.rate_limit - elapsed)
        
        response = self.session.get(url, timeout=self.timeout, **kwargs)
        self.last_request_time = time.time()
        return response
    
    def analyze(self, url: str) -> Dict[str, Any]:
        """
        Analyze permissions and accessibility.
        
        Returns:
            Dict with score, allowed/blocked agents, and metadata
        """
        score = 100
        result = {
            'allowed_agents': [],
            'blocked_agents': [],
            'llms_txt_present': False,
            'response_time_ms': 0,
            'http_status': 200
        }
        
        parsed = urlparse(url)
        base_url = f"{parsed.scheme}://{parsed.netloc}"
        
        try:
            # Check main URL response
            start_time = time.time()
            response = self._rate_limited_request(url)
            result['response_time_ms'] = round((time.time() - start_time) * 1000)
            result['http_status'] = response.status_code
            
            if response.status_code in [401, 403]:
                return {
                    **result,
                    'score': 0,
                    'note': f'Access forbidden (HTTP {response.status_code})'
                }
            
            # Response time penalty (more lenient)
            if result['response_time_ms'] > self.SLOW_RESPONSE_MS:
                score -= 10
            elif result['response_time_ms'] > 1500:
                score -= 5
            
            # Check robots.txt
            try:
                robots_response = self._rate_limited_request(f"{base_url}/robots.txt")
                if robots_response.status_code == 200:
                    rp = RobotFileParser()
                    rp.parse(robots_response.text.split('\n'))
                    
                    for agent in self.AI_AGENTS:
                        test_path = parsed.path if parsed.path else '/'
                        if rp.can_fetch(agent, urljoin(url, test_path)):
                            result['allowed_agents'].append(agent)
                        else:
                            result['blocked_agents'].append(agent)
                            score -= 10  # Reduced from 15
            except Exception:
                # If robots.txt fails, assume all agents allowed
                result['allowed_agents'] = self.AI_AGENTS
            
            # Check for llms.txt
            try:
                for path in ['/llms.txt', '/.well-known/llms.txt']:
                    llms_response = self._rate_limited_request(base_url + path)
                    if llms_response.status_code == 200 and len(llms_response.text) > 10:
                        result['llms_txt_present'] = True
                        score = max(score, 80)  # Bonus for llms.txt
                        break
            except Exception:
                pass
            
            result['score'] = max(0, score)
            return result
            
        except Exception as e:
            return {
                **result,
                'score': 0,
                'error': str(e),
                'note': f'Error: {str(e)}'
            }
