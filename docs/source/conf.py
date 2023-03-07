# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import sys
from pathlib import Path
source_code_relative_path = Path('../..')
source_code_abs_path = source_code_relative_path.resolve()
sys.path.insert(0, f'{source_code_abs_path}')
from project import __version__


# -- Project information -----------------------------------------------------

project = 'ifrs16'
copyright = '2023, Bradley Smith'
author = 'Bradley Smith'
version = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'press'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

favicon_path = source_code_abs_path / 'graphics/favicon.png'
html_favicon = f'{favicon_path}'

logo_path = source_code_abs_path / 'graphics/favicon.png'
html_logo = f'{logo_path}'


extlinks = {
    'wheel_url': (
        f'https://github.com/bradley-smith-gpa/sphinx-test/releases/download/{version}/ifrs16-{version}-py3-none-any.whl',
        'wheel version %s'
    )
}
