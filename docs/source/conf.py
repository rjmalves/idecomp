import os
import sys
from datetime import date
import plotly.io as pio

pio.renderers.default = "sphinx_gallery"

sys.path.insert(0, os.path.abspath("../../"))
from idecomp import __version__  # noqa: E402

project = "idecomp"
copyright = f"{date.today().year}, Rogerio Alves"
author = "Rogerio Alves"

# The full version, including alpha/beta/rc tags
release = __version__
today = date.today().strftime("%d/%m/%Y")

extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx_gallery.gen_gallery",
    "numpydoc",
]

autosummary_generate = True
templates_path = ["_templates"]
language = "pt_BR"
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
exclude_patterns: list[str] = []

add_module_names = False
pygments_style = "friendly"
pygments_dark_style = "monokai"
modindex_common_prefix = ["idecomp."]

html_theme = "furo"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#2962ff",
        "color-brand-content": "#2962ff",
    },
    "dark_css_variables": {
        "color-brand-primary": "#5c8aff",
        "color-brand-content": "#5c8aff",
    },
    "sidebar_hide_name": True,
}

html_static_path = ["_static"]
html_logo = "_static/logo_idecomp_svg.svg"

default_role = "obj"

numpydoc_show_class_members = False
intersphinx_mapping = {
    "python": (
        "https://docs.python.org/{.major}".format(sys.version_info),
        None,
    ),
    "pandas": ("http://pandas.pydata.org/pandas-docs/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "cfinterface": ("https://rjmalves.github.io/cfinterface/", None),
}

sphinx_gallery_conf = {
    "examples_dirs": "../../examples",
    "gallery_dirs": "examples",
    "backreferences_dir": "gen_modules/generated",
}
