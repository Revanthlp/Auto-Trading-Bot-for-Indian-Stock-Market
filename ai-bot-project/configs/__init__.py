import os
from typing import Dict, Any
import json

def load_config() -> Dict[str, Any]:
    """Load main configuration"""
    with open(os.path.join(os.path.dirname(__file__), 'config.json')) as f:
        return json.load(f)

__all__ = ['load_config']