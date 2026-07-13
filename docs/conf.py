# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# NOTE: This file is designed to be synced across all IATI documentation repos.
# Project-specific settings are imported from project_info.py.

import os
import sys

import sphinx.application
from sphinx.locale import get_translation

import iati_sphinx_theme

# Make project_info importable regardless of how Sphinx is invoked. `python -m
# sphinx`/sphinx-autobuild add the current working directory to sys.path
# automatically when run from this directory, but installed console scripts
# like `sphinx-build` (e.g. via `make latexpdf`) don't - their sys.path[0] is
# their own bin directory instead.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import project-specific settings
from project_info import (
    project,
    tool_url,
    nav_label,
    eyebrow_text,
    github_repository,
    languages,
    plausible_domain,
    redoc,
)

# Derive nav and title from project_info. When tool_url is set, the
# header shows two nav items: the tool itself, and a self-link to the
# documentation. When unset, just the self-link.
_nav_label = nav_label or project
if tool_url:
    tool_nav_items = {_nav_label: tool_url}
    project_title = f"{_nav_label}: Documentation"
else:
    tool_nav_items = {}
    project_title = project

MESSAGE_CATALOG_NAME = "iati-sphinx-theme"
_ = get_translation(MESSAGE_CATALOG_NAME)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

author = "IATI Secretariat"
language = "en"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinxcontrib.redoc",
    "sphinxcontrib.video",
    "sphinxcontrib.youtube",
    "iati_sphinx_theme",  # Register theme as extension for LaTeX defaults
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "iati_sphinx_theme"
html_theme_options = {  # See https://iati-sphinx-theme.readthedocs-hosted.com/en/latest/#configuration for additional options and info
    "github_repository": github_repository,
    "header_title_text": _(project),
    "header_eyebrow_text": _(eyebrow_text),
    "languages": languages,
    "plausible_domain": plausible_domain,
    "project_title": _(project_title),
    "show_download_links": True,
    "tool_nav_items": tool_nav_items,
}

# Add any paths that contain custom static files (such as style sheets, videos,
# images) here, relative to this directory. They are copied after the builtin
# static files, so a file named "default.css" will overwrite the builtin
# "default.css".
html_static_path = ["_static"]

todo_include_todos = True

html_context = {}

# -- Options for LaTeX/PDF output -----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#latex-options

latex_documents = [
    (
        "index",  # startdocname
        "iati-docs-base.tex",  # targetname
        project_title,  # title
        author,  # author
        "manual",  # theme
    ),
]

if os.environ.get("READTHEDOCS") == "True":
    project_slug = os.environ.get("READTHEDOCS_PROJECT")
    version_slug = os.environ.get("READTHEDOCS_VERSION")
    language_slug = os.environ.get("READTHEDOCS_LANGUAGE", "en")

    # RTD's standard download URL pattern
    pdf_url = f"https://{project_slug}.readthedocs-hosted.com/_/downloads/{language_slug}/{version_slug}/pdf/"

    html_context["pdf_url"] = pdf_url
else:
    # Local dev builds have no RTD-hosted PDF. `make latexpdf` (wired up as
    # a preLaunchTask in .vscode/tasks.json) builds one alongside the HTML
    # output instead - only link to it if that's actually happened, so a
    # plain `make html` or a terminal `sphinx-autobuild` run (which don't
    # build the PDF) doesn't show a link that 404s.
    pdf_filename = latex_documents[0][1].replace(".tex", ".pdf")
    pdf_path = os.path.join(os.path.dirname(__file__), "_build", "html", pdf_filename)
    if os.path.exists(pdf_path):
        html_context["pdf_url"] = f"/{pdf_filename}"

# -- Options for Texinfo output -------------------------------------------

locale_dirs = [
    "locale",
    os.path.join(os.path.dirname(iati_sphinx_theme.__file__), "locale"),
]


def setup(app: sphinx.application.Sphinx) -> None:
    locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "locale")
    app.add_message_catalog(MESSAGE_CATALOG_NAME, locale_path)
