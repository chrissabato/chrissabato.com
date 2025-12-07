# This file is used for building the site for deployment (publishing).
# It inherits settings from pelicanconf.py and overrides production-specific values.

import os
import sys
# Make sure your main config file is in the same directory
sys.path.append(os.curdir)
from pelicanconf import *

# --- Production Overrides ---
# 1. Set the definitive SITEURL for production (Crucial for correct absolute links)
# Replace 'ssh-user' and 'your-domain.com' with your actual server details
SITEURL = 'https://chrissabato.com'
RELATIVE_URLS = False # Must be False for production

# 2. Disable unnecessary feeds for production
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# 3. Configure the deployment command using rsync over SSH
# This is the key to sending your files to the server.
#
# Replace:
#   - 'ssh-user' with your SSH username (e.g., 'root' or 'ubuntu')
#   - 'your-domain.com' with your server's domain or IP
#   - '/var/www/your-site/' with the absolute path on your server where the files should go
#
# rsync - delete: deletes files in the remote folder that are no longer locally in the output folder
# rsync - r: recursive copy
# rsync - v: verbose
# rsync - z: compress file data during the transfer
# rsync - e: specifies the remote shell to use (ssh in this case)
#
# The variable {output} is automatically replaced by Pelican with the path to your 'output' directory.
SSH_USER = "chrissabato"
SSH_HOST = "chrissabato.com"
SSH_PORT = 22
SSH_TARGET_PATH = "/home/chrissabato/www/chrissabato.com/html"

# Note: scp does not offer the '--delete' safety feature of rsync.
try:
    # Use scp for recursive copy. Windows uses 'scp -r' which can be more reliable than trying to execute rsync.
    PUBLISH_COMMAND = f'scp -r -P {SSH_PORT} {{output}}/* {SSH_USER}@{SSH_HOST}:{SSH_TARGET_PATH}'
except NameError:
    # Fallback command
    PUBLISH_COMMAND = 'scp -r -P 22 {output}/* chrissabato@chrissabato.com:/home/chrissabato/www/chrissabato.com/html/'

# --- Deployment Tool ---
# You can also use the FABRIC integration if you prefer
# FABRIC = {
#     'host_string': f'{SSH_USER}@{SSH_HOST}:{SSH_PORT}',
#     'deploy_path': SSH_TARGET_PATH,
# }