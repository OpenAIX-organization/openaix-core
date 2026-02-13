"""
Data storage utilities for OpenAIX evaluations.

Provides standardized directory structure:
data/evaluations/YYYYMMDD/
  - {timestamp}_{site_name}.json
  - {timestamp}_{site_name}.md
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


class EvaluationStorage:
    """Manages evaluation data storage with date-based directory structure."""
    
    BASE_DIR = 'data/evaluations'
    
    def __init__(self, custom_date: Optional[str] = None):
        """
        Initialize storage with optional custom date.
        
        Args:
            custom_date: Date string in format 'YYYYMMDD'. If None, uses today.
        """
        if custom_date:
            self.date_str = custom_date
        else:
            self.date_str = datetime.now().strftime('%Y%m%d')
        
        self.storage_dir = Path(self.BASE_DIR) / self.date_str
        self._ensure_directory()
    
    def _ensure_directory(self):
        """Create storage directory if it doesn't exist."""
        self.storage_dir.mkdir(parents=True, exist_ok=True)
    
    def save_evaluation(self, result: Dict[str, Any], 
                       filename_prefix: Optional[str] = None,
                       formats: list = ['json', 'md']) -> Dict[str, str]:
        """
        Save evaluation result to standardized location.
        
        Args:
            result: The evaluation result dictionary
            filename_prefix: Optional prefix for filename (default: site domain)
            formats: List of formats to save ('json', 'md')
        
        Returns:
            Dict mapping format to saved file path
        """
        # Generate filename prefix from URL if not provided
        if not filename_prefix:
            url = result.get('target', 'unknown')
            filename_prefix = self._url_to_filename(url)
        
        # Generate timestamp
        timestamp = datetime.now().strftime('%H%M%S')
        
        saved_files = {}
        
        # Save JSON
        if 'json' in formats:
            json_path = self._save_json(result, filename_prefix, timestamp)
            saved_files['json'] = str(json_path)
        
        # Save Markdown
        if 'md' in formats:
            md_path = self._save_markdown(result, filename_prefix, timestamp)
            saved_files['md'] = str(md_path)
        
        return saved_files
    
    def _url_to_filename(self, url: str) -> str:
        """Convert URL to safe filename."""
        from urllib.parse import urlparse
        
        parsed = urlparse(url)
        domain = parsed.netloc.replace('www.', '')
        
        # Remove special characters
        safe_name = domain.replace('.', '_').replace('-', '_')
        
        return safe_name
    
    def _save_json(self, result: Dict[str, Any], 
                   prefix: str, timestamp: str) -> Path:
        """Save result as JSON file."""
        filename = f"{timestamp}_{prefix}.json"
        filepath = self.storage_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def _save_markdown(self, result: Dict[str, Any], 
                       prefix: str, timestamp: str) -> Path:
        """Save result as Markdown report."""
        filename = f"{timestamp}_{prefix}.md"
        filepath = self.storage_dir / filename
        
        md_content = self._generate_markdown(result)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        return filepath
    
    def _generate_markdown(self, result: Dict[str, Any]) -> str:
        """Generate markdown report from result."""
        lines = []
        
        # Header
        lines.append(f"# OpenAIX Evaluation Report")
        lines.append(f"\n**Target**: {result.get('target', 'N/A')}")
        lines.append(f"**Score**: {result.get('score', 0)}/100")
        lines.append(f"**Grade**: {result.get('grade', 'N/A')}")
        lines.append(f"**Timestamp**: {result.get('timestamp', 'N/A')}")
        
        # Site type info (if available)
        site_type = result.get('site_type', {})
        if site_type:
            lines.append(f"**Site Type**: {site_type.get('type', 'unknown')} "
                        f"(confidence: {site_type.get('confidence', 0)}%)")
        
        lines.append(f"\n---\n")
        
        # Metrics
        lines.append("## Metrics\n")
        metrics = result.get('metrics', {})
        for key, value in metrics.items():
            lines.append(f"- **{key}**: {value}")
        
        # Dimensions
        lines.append(f"\n---\n")
        lines.append("## Dimensions\n")
        dimensions = result.get('dimensions', {})
        for dim_name, dim_data in dimensions.items():
            if isinstance(dim_data, dict) and 'score' in dim_data:
                lines.append(f"\n### {dim_name.replace('_', ' ').title()}")
                lines.append(f"- Score: {dim_data['score']}")
                for k, v in dim_data.items():
                    if k != 'score':
                        lines.append(f"- {k}: {v}")
        
        # Suggestions
        lines.append(f"\n---\n")
        lines.append("## Suggestions\n")
        suggestions = result.get('suggestions', [])
        for suggestion in suggestions:
            lines.append(f"- {suggestion}")
        
        return '\n'.join(lines)
    
    def list_evaluations(self, date: Optional[str] = None) -> list:
        """List all evaluations for a given date."""
        if date:
            target_dir = Path(self.BASE_DIR) / date
        else:
            target_dir = self.storage_dir
        
        if not target_dir.exists():
            return []
        
        files = list(target_dir.glob('*.json'))
        files.extend(target_dir.glob('*.md'))
        
        return [str(f.relative_to(self.BASE_DIR)) for f in files]
    
    def load_evaluation(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load a specific evaluation by filename."""
        filepath = Path(self.BASE_DIR) / filename
        
        if not filepath.exists():
            return None
        
        if filepath.suffix == '.json':
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return None
    
    def get_storage_path(self) -> str:
        """Get current storage directory path."""
        return str(self.storage_dir)


def save_evaluation(result: Dict[str, Any], 
                   date: Optional[str] = None,
                   filename_prefix: Optional[str] = None,
                   formats: list = ['json', 'md']) -> Dict[str, str]:
    """
    Convenience function to save evaluation.
    
    Usage:
        from openaix.storage import save_evaluation
        
        result = scorer.score('https://example.com')
        files = save_evaluation(result)
        # Returns: {'json': 'data/evaluations/20260213/143052_example_com.json', 
        #           'md': 'data/evaluations/20260213/143052_example_com.md'}
    """
    storage = EvaluationStorage(date)
    return storage.save_evaluation(result, filename_prefix, formats)
