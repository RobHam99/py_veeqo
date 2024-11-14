# mypackage/__init__.py
import os

def read_version():
    version_file = os.path.join(os.path.dirname(__file__), 'version.txt')
    if os.path.exists(version_file):
        with open(version_file) as f:
            return f.read().strip()
    return "0.0.1"  # Default version if not found

__version__ = read_version()
