import sys

MIN_PYTHON = (3, 8)
if sys.version_info < MIN_PYTHON:
    sys.exit("Please use Python %s.%s or later.\n" % MIN_PYTHON)

from .auscultor import *
