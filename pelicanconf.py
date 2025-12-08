AUTHOR = 'Chris Sabato'
SITENAME = 'Chris Sabato'
SITENAME_LETTERS = 'CS'
SITEURL = ""

#PATH = 'content'
PATH = 'content/test-publish'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'English'

# --- Custom Settings for Folder-per-Post Structure ---
# 1. PATH_METADATA ensures directory names are not used as categories/slugs
PATH_METADATA = '(?P<slug>.*)\\..*' 

# 2. Ensures posts without a Category metadata field default to 'General'
DEFAULT_CATEGORY = 'General' 

# 3. Tell Pelican to copy static assets (like images) from the 'content' folders
# If you want everything copied that isn't an article, use STATIC_PATHS = ['.']
# For simplicity, we assume assets are directly inside content/post-folder/
STATIC_PATHS = ['.'] 

# 4. IGNORE_FILES prevents temporary files (like editor autosaves) from being processed
IGNORE_FILES = ['.#*', '.DS_Store', '*.bak']
# ---------------------------------------------------

DELETE_OUTPUT_DIRECTORY = True

MARKUP = ('md',)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "themes/sabato"

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja2/"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True