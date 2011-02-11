# coding: utf-8
# 
# put.io xbmc addon
# Copyright (C) 2009  Alper Kanat <alper@put.io>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
# 

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