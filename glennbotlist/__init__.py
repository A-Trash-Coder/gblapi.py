from .GBL import GBL
from glennbotlist import errors
from .bot import Bot
from .WebhookServer import WebhookServer

__copyright__ = 'Copyright 2020 Gavyn Stanley'
__author__ = "Gavyn Stanley (A Trash Coder)"
__license__ = "MIT"
__title__ = "gblapi.py"
__version__ = "0.3.0"

from collections import namedtuple

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major = 0, minor = 3, micro = 0, releaselevel = 'final', serial = 0)