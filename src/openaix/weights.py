"""
Dynamic weights configuration for OpenAIX Scorer v1.1

Five dimensions with adjustable weights based on site type.
"""

from typing import Dict

# Weight profiles for different site types
WEIGHT_PROFILES = {
    'documentation': {
        'snr': 0.35,
        'semantic': 0.25,
        'token_economy': 0.20,
        'permissions': 0.10,
        'api_availability': 0.10
    },
    'product': {
        'snr': 0.25,
        'semantic': 0.35,
        'token_economy': 0.15,
        'permissions': 0.10,
        'api_availability': 0.15
    },
    'platform': {
        'snr': 0.15,
        'semantic': 0.25,
        'token_economy': 0.15,
        'permissions': 0.10,
        'api_availability': 0.35
    },
    'content': {
        'snr': 0.30,
        'semantic': 0.25,
        'token_economy': 0.25,
        'permissions': 0.10,
        'api_availability': 0.10
    },
    'default': {
        'snr': 0.25,
        'semantic': 0.30,
        'token_economy': 0.20,
        'permissions': 0.15,
        'api_availability': 0.10
    }
}

# Site type descriptions for reporting
SITE_TYPE_DESCRIPTIONS = {
    'documentation': 'Documentation sites (high SNR, clear structure)',
    'product': 'Product sites (visual-rich, needs structured data)',
    'platform': 'Platform sites (API-first, CLI tools, multi-page)',
    'content': 'Content sites (text-heavy, narrative)',
    'default': 'General sites (balanced weights)'
}


def get_weights(site_type: str) -> Dict[str, float]:
    """Get weight profile for a site type."""
    return WEIGHT_PROFILES.get(site_type, WEIGHT_PROFILES['default'])


def get_site_description(site_type: str) -> str:
    """Get human-readable description of site type."""
    return SITE_TYPE_DESCRIPTIONS.get(site_type, SITE_TYPE_DESCRIPTIONS['default'])
