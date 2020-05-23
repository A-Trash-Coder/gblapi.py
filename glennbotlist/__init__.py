from .GBL import GBL
from .GBL import errors

__copyright__ = 'Copyright 2020 Gavyn Stanley'
__author__ = "Gavyn Stanley (A Trash Coder)"
__license__ = "MIT"
__title__ = "gblapi.py"
__version__ = "0.2.2"

from collections import namedtuple

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major = 0, minor = 2, micro = 2, releaselevel = 'final', serial = 0)