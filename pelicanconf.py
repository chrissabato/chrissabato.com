AUTHOR = 'Chris Sabato'
SITENAME = 'Chris Sabato'
SITENAME_LETTERS = 'CS'
SITEURL = ""

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DEFAULT_LANG = 'en'


PATH_METADATA = r'(?P<slug>.*)\..*' 

DEFAULT_CATEGORY = 'General' 

# 3. Tell Pelican to copy static assets (like images) from the 'content' folders
# If you want everything copied that isn't an article, use STATIC_PATHS = ['.']
# For simplicity, we assume assets are directly inside content/post-folder/
STATIC_PATHS = ['.'] 

# 4. IGNORE_FILES prevents temporary files (like editor autosaves) from being processed
IGNORE_FILES = ['.#*', '.DS_Store', '*.bak']
# ---------------------------------------------------

DELETE_OUTPUT_DIRECTORY = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "themes/sabato"

MARKDOWN = {
    'extension_configs': {
        'markdown_include.include': {
            'base_path': 'content',
        },
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}


# --- Web editor (Sveltia CMS at /admin/) -----------------------------------
# content/admin/ holds the editor page; copy it as static files instead of
# treating index.html as an article.
ARTICLE_EXCLUDES = ['admin']
PAGE_EXCLUDES = ['admin']

# cms_frontmatter cleans up the YAML the editor writes so Pelican reads it the
# same way as hand-written posts. Listing PLUGINS turns off auto-discovery, so
# data_files (from pelican-data-files) has to be named here too.
PLUGIN_PATHS = ['plugins']
PLUGINS = ['cms_frontmatter', 'pelican.plugins.data_files']
