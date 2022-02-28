import re
import sys


MODULE_REGEX = r'^[-a-zA-Z][-a-zA-Z0-9_]+$'

github_proj = '{{cookiecutter.github_proj}}'

if not re.match(MODULE_REGEX, github_proj):
    print('ERROR: %s is not a valid project name!' % github_proj)

    # exits with status 1 to indicate failure
    sys.exit(1)
