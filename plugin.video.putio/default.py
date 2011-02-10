# coding: utf-8

import os
import sys

import xbmc

# adding lib to python path (just for simplejson)
sys.path.append(os.path.join(os.getcwd(), "resources", "lib"))

from resources.lib.common import PutIO
from resources.lib.gui import populateDir

pluginUrl = sys.argv[0]
pluginId = int(sys.argv[1])
itemId = sys.argv[2].replace("?", "")

putio = PutIO(pluginId)

if itemId == "":
    populateDir(pluginUrl, pluginId, putio.getRootListing())
else:
    populateDir(pluginUrl, pluginId, putio.getFolderListing(itemId))