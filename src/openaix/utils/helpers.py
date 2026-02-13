"""
Utility functions for OpenAIX Scorer.
"""

import re
from typing import Set
from urllib.parse import urljoin, urlparse


def normalize_url(url: str) -> str:
    """Normalize URL by adding https:// if missing."""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url


def extract_words(text: str) -> Set[str]:
    """Extract words from text for similarity comparison."""
    if not text:
        return set()
    return set(re.findall(r'\b\w+\b', text.lower()))


def text_similarity(text1: str, text2: str) -> float:
    """
    Calculate text similarity using Jaccard similarity.
    Returns value between 0 and 1.
    """
    words1 = extract_words(text1)
    words2 = extract_words(text2)
    
    if not words1 and not words2:
        return 1.0
    if not words1 or not words2:
        return 0.0
    
    intersection = words1 & words2
    union = words1 | words2
    
    return len(intersection) / len(union)


def get_timestamp() -> str:
    """Get current UTC timestamp in ISO format."""
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
