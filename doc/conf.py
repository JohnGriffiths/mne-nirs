# -*- coding: utf-8 -*-
#
# project-template documentation build configuration file, created by
# sphinx-quickstart on Mon Jan 18 14:44:12 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import datetime, timezone
import sys
import os
import warnings
from sphinx_gallery.sorting import FileNameSortKey

sys.path.append("../")
import mne
from mne.fixes import _compare_version
from mne_nirs import __version__  # noqa: E402
from mne.tests.test_docstring_parameters import error_ignores


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx_fontawesome',
    'sphinx_gallery.gen_gallery',
    'numpydoc',
    'sphinxcontrib.bibtex',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# generate autosummary even if no references.
autosummary_generate = True
autodoc_default_options = {'inherited-members': None}

# The suffix of source filenames.
source_suffix = '.rst'

# Generate the plots for the gallery
plot_gallery = 'True'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'MNE-NIRS'
td = datetime.now(tz=timezone.utc)

# We need to triage which date type we use so that incremental builds work
# (Sphinx looks at variable changes and rewrites all files if some change)
copyright = (
    f'2012–{td.year}, MNE Developers. Last updated <time datetime="{td.isoformat()}" class="localized">{td.strftime("%Y-%m-%d %H:%M %Z")}</time>\n'  # noqa: E501
    '<script type="text/javascript">$(function () { $("time.localized").each(function () { var el = $(this); el.text(new Date(el.attr("datetime")).toLocaleString([], {dateStyle: "medium", timeStyle: "long"})); }); } )</script>')  # noqa: E501
if os.getenv('MNE_FULL_DATE', 'false').lower() != 'true':
    copyright = f'2012–{td.year}, MNE Developers. Last updated locally.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '_templates']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# NumPyDoc configuration -----------------------------------------------------

numpydoc_class_members_toctree = False
numpydoc_attributes_as_param_list = True
numpydoc_validate = True
numpydoc_validation_checks = {'all'} | set(error_ignores)
numpydoc_validation_exclude = {  # set of regex
    # dict subclasses
    r'\.clear', r'\.get$', r'\.copy$', r'\.fromkeys', r'\.items', r'\.keys',
    r'\.pop', r'\.popitem', r'\.setdefault', r'\.update', r'\.values',
    # list subclasses
    r'\.append', r'\.count', r'\.extend', r'\.index', r'\.insert', r'\.remove',
    r'\.sort',
    # we currently don't document these properly (probably okay)
    r'\.__getitem__', r'\.__contains__', r'\.__hash__', r'\.__mul__',
    r'\.__sub__', r'\.__add__', r'\.__iter__', r'\.__div__', r'\.__neg__',
    # copied from sklearn
    r'mne\.utils\.deprecated',
}


# sphinxcontrib-bibtex
bibtex_bibfiles = ['./references.bib', './references-nirs.bib']
bibtex_style = 'unsrt'
bibtex_footbibliography_header = ''


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}
switcher_version_match = 'dev' if release.endswith('dev0') else version
html_theme_options = {
    'github_url': 'https://github.com/mne-tools/mne-nirs',
    "show_toc_level": 1,
    'navbar_end': ['version-switcher', 'navbar-icon-links'],
    'footer_items': ['copyright'],
    "google_analytics_id": "UA-188272121-1",
    'switcher': {
        'json_url': 'https://mne.tools/mne-nirs/dev/_static/versions.json',
        'version_match': switcher_version_match,
    }
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'mnenirsdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'project-template.tex', u'project-template Documentation',
     u'Robert Luke', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'project-template', u'project-template Documentation',
     [u'Robert Luke'], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'project-template', u'project-template Documentation',
     u'Robert Luke', 'project-template', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(
        sys.version_info), None),
    'numpy': ('https://numpy.org/devdocs', None),
    'scipy': ('https://scipy.github.io/devdocs', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
    'mne': ('https://mne.tools/stable', None),
    'nilearn': ('http://nilearn.github.io/stable', None),
    'sklearn': ('https://scikit-learn.org/stable', None),
    'mne_bids': ('https://mne.tools/mne-bids/stable', None),
    'statsmodels': ('https://www.statsmodels.org/stable', None)
}

scrapers = ('matplotlib',)
try:
    mne.viz.set_3d_backend(mne.viz.get_3d_backend())
except Exception:
    report_scraper = None
else:
    backend = mne.viz.get_3d_backend()
    if backend == 'mayavi':
        from traits.api import push_exception_handler
        mlab = mne.utils._import_mlab()
        # Do not pop up any mayavi windows while running the
        # examples. These are very annoying since they steal the focus.
        mlab.options.offscreen = True
        # hack to initialize the Mayavi Engine
        mlab.test_plot3d()
        mlab.close()
        scrapers += ('mayavi',)
        push_exception_handler(reraise_exceptions=True)
    elif backend in ('notebook', 'pyvistaqt'):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            import pyvista
        pyvista.OFF_SCREEN = False
        brain_scraper = mne.viz._brain._BrainScraper()
        scrapers += (brain_scraper, 'pyvista')
    report_scraper = mne.report._ReportScraper()
    scrapers += (report_scraper,)
    del backend
try:
    import mne_qt_browser
    _min_ver = _compare_version(mne_qt_browser.__version__, '>=', '0.2')
    if mne.viz.get_browser_backend() == 'qt' and _min_ver:
        scrapers += (mne.viz._scraper._MNEQtBrowserScraper(),)
except ImportError:
    pass

# Resolve binder filepath_prefix. From the docs:
# "A prefix to append to the filepath in the Binder links. You should use this
# if you will store your built documentation in a sub-folder of a repository,
# instead of in the root."
# we will store dev docs in a `dev` subdirectory and all other docs in a
# directory "v" + version_str. E.g., "v0.3"
if 'dev' in version:
    filepath_prefix = 'dev'
else:
    filepath_prefix = 'stable'

# sphinx-gallery configuration
sphinx_gallery_conf = {
    'doc_module': 'mne_nirs',
    'backreferences_dir': os.path.join('generated'),
    'image_scrapers': scrapers,
    'reference_url': {
        'mne_nirs': None},
    'download_all_examples': False,
    'show_memory': True,
    'within_subsection_order': FileNameSortKey,
    'junit': os.path.join('..', 'test-results', 'sphinx-gallery', 'junit.xml'),
    'binder': {
    # Required keys
    'org': 'mne-tools',
    'repo': 'mne-nirs',
    'branch': 'gh-pages',  # noqa: E501 Can be any branch, tag, or commit hash. Use a branch that hosts your docs.
    'binderhub_url': 'https://mybinder.org',  # noqa: E501 Any URL of a binderhub deployment. Must be full URL (e.g. https://mybinder.org).
        'filepath_prefix': filepath_prefix,  # noqa: E501 A prefix to prepend to any filepaths in Binder links.
        'dependencies': [
            '../requirements.txt',
            '../requirements_doc.txt',
        ],
    },
    'plot_gallery': 'True',  # Avoid annoying str/bool default warning
}


def setup(app):
    # a copy button to copy snippet of code from the documentation
    app.add_js_file('js/copybutton.js')
    app.add_css_file('font-awesome.css')
