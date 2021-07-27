# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "powerplantmatching"
copyright = "2021, Fabian Hofmann, Fabian Gotzens, Jonas Hörsch, Martha Frysztacki"
author = "Fabian Hofmann, Fabian Gotzens, Jonas Hörsch, Martha Frysztacki"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_automodapi.automodapi",  # for api reference
    "nbsphinx",
    "sphinx.ext.imgconverter",  # for SVG conversion
]
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "display_version": True,
    "sticky_navigation": True,
    # 'style_nav_header_background': '#009682',
}


# Add any paths that contain custom themes here, relative to this directory.
html_static_path = ["_static"]

html_context = {
    "css_files": ["_static/theme_overrides.css"]  # override wide tables in RTD theme
}

# -- Options for nbsphinx -------------------------------------------------
nbsphinx_execute = "never"
