"""
API Availability scoring dimension.

Evaluates whether the website provides programmatic access via APIs,
CLI tools, or machine-readable endpoints.
"""

import re
from typing import Dict, Any, List
from urllib.parse import urlparse
import requests


class APIAvailabilityAnalyzer:
    """Analyzes API availability for AI agents."""
    
    # Endpoints to check for OpenAPI/Swagger
    OPENAPI_ENDPOINTS = [
        '/openapi.json',
        '/swagger.json',
        '/api-docs',
        '/swagger-ui.html',
        '/api/v1/openapi.json',
        '/api/openapi.json'
    ]
    
    # API documentation paths
    API_DOC_PATHS = [
        '/api',
        '/docs/api',
        '/developers',
        '/api-reference',
        '/reference/api',
        '/documentation/api'
    ]
    
    # CLI tool indicators in HTML/llms.txt
    CLI_INDICATORS = [
        'npm install -g',
        'pip install',
        'cargo install',
        'brew install',
        'apt install',
        'yum install',
        'cli', 'command line', 'terminal',
        'command-line interface',
        'gh ', 'vercel ', 'netlify ', 'stripe ',
        'brew tap'
    ]
    
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.session = requests.Session()
    
    def analyze(self, base_url: str, html: str = None) -> Dict[str, Any]:
        """
        Analyze API availability.
        
        Returns:
            Dict with score (0-100), features list, and endpoints found
        """
        score = 0
        features = []
        endpoints_found = []
        
        # 1. Check OpenAPI/Swagger Spec (30 points)
        openapi_result = self._check_openapi(base_url)
        if openapi_result:
            score += 30
            features.append('openapi_spec')
            endpoints_found.append(openapi_result)
        
        # 2. Check GraphQL Endpoint (25 points)
        if self._check_graphql(base_url):
            score += 25
            features.append('graphql')
            endpoints_found.append(f"{base_url}/graphql")
        
        # 3. Check API Subdomain (20 points)
        api_subdomain = self._check_api_subdomain(base_url)
        if api_subdomain:
            score += 20
            features.append('api_subdomain')
            endpoints_found.append(api_subdomain)
        
        # 4. Check API Documentation (15 points)
        api_docs = self._check_api_docs(base_url)
        if api_docs:
            score += 15
            features.append('api_docs')
            endpoints_found.append(api_docs)
        
        # 5. Check CLI Tool Availability (10 points)
        if html and self._detect_cli_tool(html, base_url):
            score += 10
            features.append('cli_tool')
        
        return {
            'score': min(100, score),
            'features': features,
            'endpoints_found': endpoints_found,
            'has_api': score >= 15,  # At least API docs
            'has_comprehensive_api': score >= 60  # Multiple API features
        }
    
    def _check_openapi(self, base_url: str) -> str:
        """Check for OpenAPI/Swagger specification."""
        for endpoint in self.OPENAPI_ENDPOINTS:
            url = f"{base_url.rstrip('/')}{endpoint}"
            try:
                response = self.session.get(url, timeout=self.timeout)
                if response.status_code == 200:
                    content = response.text.strip()
                    # Verify it's actually OpenAPI spec
                    if '"openapi"' in content or '"swagger"' in content:
                        return url
            except:
                continue
        return None
    
    def _check_graphql(self, base_url: str) -> bool:
        """Check for GraphQL endpoint."""
        url = f"{base_url.rstrip('/')}/graphql"
        try:
            response = self.session.get(url, timeout=self.timeout)
            if response.status_code == 200:
                content = response.text.lower()
                # GraphQL endpoints usually return a playground or error message
                if 'graphql' in content or '__schema' in content or 'query' in content:
                    return True
            # Also try POST with introspection query
            post_response = self.session.post(
                url,
                json={'query': '{__schema{types{name}}}'},
                timeout=self.timeout
            )
            if post_response.status_code == 200:
                return True
        except:
            pass
        return False
    
    def _check_api_subdomain(self, base_url: str) -> str:
        """Check for api.* subdomain."""
        parsed = urlparse(base_url)
        domain = parsed.netloc
        
        # Remove www. if present
        if domain.startswith('www.'):
            domain = domain[4:]
        
        api_url = f"{parsed.scheme}://api.{domain}"
        try:
            response = self.session.get(api_url, timeout=self.timeout, allow_redirects=True)
            if response.status_code in [200, 401, 403]:  # 401/403 means API exists but needs auth
                return api_url
        except:
            pass
        return None
    
    def _check_api_docs(self, base_url: str) -> str:
        """Check for API documentation pages."""
        for path in self.API_DOC_PATHS:
            url = f"{base_url.rstrip('/')}{path}"
            try:
                response = self.session.get(url, timeout=self.timeout)
                if response.status_code == 200:
                    return url
            except:
                continue
        return None
    
    def _detect_cli_tool(self, html: str, base_url: str) -> bool:
        """Detect CLI tool availability."""
        html_lower = html.lower()
        
        # Check HTML content for CLI indicators
        for indicator in self.CLI_INDICATORS:
            if indicator.lower() in html_lower:
                return True
        
        # Check llms.txt for CLI mention
        try:
            llms_url = f"{base_url.rstrip('/')}/llms.txt"
            response = self.session.get(llms_url, timeout=self.timeout)
            if response.status_code == 200:
                llms_content = response.text.lower()
                if any(term in llms_content for term in ['cli', 'command line', 'terminal', 'npm install', 'pip install']):
                    return True
        except:
            pass
        
        return False
