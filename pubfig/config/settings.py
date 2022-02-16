"""
default settings
settings has to be all UPPER case
"""
import os
import sys

# where default and custom settings are located
SETTING_DIR = os.path.abspath(os.path.dirname(__file__))
# absolute path to base directory
if 'win' in sys.platform:   # windows system
    BASE_DIR = os.path.join(os.path.expanduser('~'), 'Desktop', 'Projects')
else:
    raise RuntimeError('operating system: {} not implemented'.format(sys.platform))

# sub directories for each project
SUB_DIRS = ['Data', 'Fig']

# plot style directory
STYLE_DIR = os.path.join(SETTING_DIR, 'styles')


