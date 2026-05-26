# Project-specific configuration for Sphinx documentation.
# This file contains settings that vary per repository.
# The main conf.py imports these values and can be synced across all repos.

# Project name (used for titles, headers, and Sphinx internals)
project = "IATI Docs Base"

# Eyebrow text: the smaller text that appears directly above the website title
eyebrow_text = "IATI Tools: Documentation"

# GitHub repository URL (for "Edit on GitHub" links)
github_repository = "https://github.com/IATI/iati-docs-base"

# Supported languages for the documentation
languages = ["en", "fr", "es"]

redoc = [
    {
        "name": "Widgets API",
        "page": "api-docs/test-widget-api",
        "spec": "specifications/test-widget-api.yaml",
        "embed": True,
        "template": "_templates/redoc-custom.j2",
    }
]

# Per-tool navigation link(s) shown in the page header. Empty for repos
# that don't represent a single tool (e.g. the docs base, multi-tool sites).
tool_nav_items = {}
