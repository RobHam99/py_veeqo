import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'py_veeqo'))

html_theme = 'sphinx_rtd_theme'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]
