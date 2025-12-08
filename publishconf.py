# This file is used for building the site for deployment (publishing).
# It inherits settings from pelicanconf.py and overrides production-specific values.

import os
import sys
# Make sure your main config file is in the same directory
sys.path.append(os.curdir)
from pelicanconf import *

# --- Production Overrides ---
SITEURL = 'https://dev.chrissabato.com'
RELATIVE_URLS = False # Must be False for production

# Disable unnecessary feeds for development/publishing if you don't use them
# However, defining them here will generate them, which is generally good practice
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# You should also ensure DELETE_OUTPUT_DIRECTORY is set correctly here
# It defaults to True if not defined, but setting it explicitly is clear:
DELETE_OUTPUT_DIRECTORY = True

MARKUP = ('md',)

# REMOVE all SSH_ and PUBLISH_COMMAND settings!