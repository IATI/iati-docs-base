# Project-specific configuration for Sphinx documentation.
# This file contains settings that vary per repository.
# The main conf.py imports these values and can be synced across all repos.

# Project name (used for titles, headers, and Sphinx internals)
project = "IATI Docs Base"

# URL of the live tool this repo documents. Set this for repos that
# document a deployed tool (Validator, Datastore, Publisher, ...).
# Leave as None for repos where the docs themselves are the deliverable
# (legal terms, handbooks, the docs base itself).
#
# When set, the page header gets a two-item nav: a link to the tool, and
# a self-link labelled "<name>: Documentation". When unset, the header
# shows a single self-link labelled with the project name.
tool_url = None

# Short label used in the nav. Defaults to ``project``. Override only
# when the project name is long and the nav needs a tighter label (e.g.
# project = "Country Development Finance Data", nav_label = "CDFD").
nav_label = None

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
