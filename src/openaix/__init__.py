"""
OpenAIX Scorer v2.1
AI Experience (AIX) Evaluation System

A modular Python package for evaluating how AI-friendly websites are.
Features: 5 dimensions, site type detection, dynamic weights, multi-page sampling.
"""

__version__ = "2.1.0"
__author__ = "OpenAIX Team"
__license__ = "MIT"

from .scorer import OpenAIXScorer
from .site_type import SiteTypeDetector
from .weights import get_weights, get_site_description

__all__ = ["OpenAIXScorer", "SiteTypeDetector", "get_weights", "get_site_description"]
