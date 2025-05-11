# Enable package-relative imports
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pytest fixtures available globally
pytest_plugins = []