import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
import responses
from bs4 import BeautifulSoup
from openaix import OpenAIXScorer
from openaix.dimensions import SNRAnalyzer, SemanticAnalyzer, TokenEconomyAnalyzer
from openaix.utils import text_similarity


class TestOpenAIXScorer:
    @pytest.fixture
    def scorer(self):
        return OpenAIXScorer(timeout=5)
    
    def test_scorer_initialization(self, scorer):
        assert scorer.timeout == 5
        assert len(scorer.WEIGHTS) == 4
    
    @responses.activate
    def test_score_success(self, scorer):
        responses.add(
            responses.GET,
            'https://example.com/robots.txt',
            body='User-agent: *\nDisallow: /admin\n',
            status=200
        )
        responses.add(
            responses.GET,
            'https://example.com',
            body='<html><body><h1>Test</h1><p>Content</p></body></html>',
            status=200
        )
        
        result = scorer.score('https://example.com')
        
        assert result['score'] >= 0
        assert 'grade' in result
        assert 'dimensions' in result
        dims = result['dimensions']
        assert 'snr' in dims
        assert 'semantic' in dims
        assert 'token_economy' in dims
        assert 'permissions' in dims


class TestSNRAnalyzer:
    def test_high_snr(self):
        analyzer = SNRAnalyzer()
        html = '<html><body><h1>Title</h1><p>Content here</p></body></html>'
        result = analyzer.analyze(html)
        
        assert result['score'] >= 80
        assert result['snr_percent'] > 30
    
    def test_low_snr(self):
        analyzer = SNRAnalyzer()
        html = '''
        <html>
        <head><style>.class{color:red}</style></head>
        <body>
            <div class="wrapper">
                <div class="content">
                    <img src="test.jpg">
                    <p>Short</p>
                </div>
            </div>
        </body>
        </html>
        '''
        result = analyzer.analyze(html)
        assert result['snr_percent'] < 30


class TestSemanticAnalyzer:
    def test_with_jsonld(self):
        analyzer = SemanticAnalyzer()
        html = '''
        <html>
        <head>
            <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@type": "Product",
                "name": "Test Product",
                "description": "A test product"
            }
            </script>
        </head>
        <body>
            <main>
                <article>
                    <h1>Title</h1>
                    <p>Content</p>
                </article>
            </main>
        </body>
        </html>
        '''
        
        soup = BeautifulSoup(html, 'lxml')
        result = analyzer.analyze(soup, 25.0)
        
        assert result['json_ld_present'] is True
        assert 'article' in result['semantic_tags_used']
        assert result['score'] > 30
    
    def test_hidden_gem_detection(self):
        analyzer = SemanticAnalyzer()
        html = '''
        <html>
        <head>
            <script type="application/ld+json">
            {"@context": "https://schema.org", "@type": "Product", 
             "name": "Product", "description": "Description"}
            </script>
        </head>
        <body>
            <div class="visual-heavy">
                <img src="hero.jpg">
                <h1>Product Name</h1>
                <p>Description</p>
            </div>
        </body>
        </html>
        '''
        
        soup = BeautifulSoup(html, 'lxml')
        result = analyzer.analyze(soup, 15.0)
        assert 'hidden_gem' in result


class TestTokenAnalyzer:
    def test_token_economy(self):
        analyzer = TokenEconomyAnalyzer()
        result = analyzer.analyze(1500)
        
        assert result['cost_rating'] == 'Low'
        assert result['score'] == 100


class TestUtils:
    def test_text_similarity_identical(self):
        similarity = text_similarity("Hello World", "Hello World")
        assert similarity == 1.0
    
    def test_text_similarity_different(self):
        similarity = text_similarity("Hello World", "Goodbye Moon")
        assert similarity < 0.3
    
    def test_text_similarity_partial(self):
        similarity = text_similarity("Hello World", "Hello There")
        assert 0 < similarity < 1.0


class TestGrading:
    def test_grade_boundaries(self):
        scorer = OpenAIXScorer()
        
        assert scorer._calculate_grade(90)['grade'].startswith('Class S')
        assert scorer._calculate_grade(75)['grade'].startswith('Class A')
        assert scorer._calculate_grade(60)['grade'].startswith('Class B')
        assert scorer._calculate_grade(40)['grade'].startswith('Class C')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
