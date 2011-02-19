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

import sys

from resources.lib.common import PutIO
from resources.lib.gui import *

pluginUrl = sys.argv[0]
pluginId = int(sys.argv[1])
itemId = sys.argv[2].lstrip("?")

putio = PutIO()

import xbmc
xbmc.log("GIVEN ITEMID: %s" % itemId)

if itemId:
    item = putio.getItem(itemId)
    
    if item.type == "folder":
        populateDir(pluginUrl, pluginId, putio.getFolderListing(itemId))
    elif item.type == "movie":
        xbmc.log("PLAYING MOVIE FILE: %s" % item.name)
        play(item, subtitle=putio.getSubtitle(item))
    else:
        xbmc.log("PLAYING NORMAL FILE %s WITH TYPE %s" % (item.name, item.type))
        play(item)
else:
    populateDir(pluginUrl, pluginId, putio.getRootListing())