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

import xbmcplugin as xp

import putio

class PutIO(object):
    """
    Class to handle putio api calls for XBMC actions
    
    """
    
    unwantedItemTypes = ("image", "compressed", "pdf", "ms_doc", "swf", "unknown")
    
    def __init__(self, pluginId):
        self.api_key = xp.getSetting(pluginId, "api_key")
        self.api_secret = xp.getSetting(pluginId, "api_secret")
        self.api = putio.Api(self.api_key, self.api_secret)
    
    def getRootListing(self):
        items = []
        
        for item in self.api.get_items(limit=50):
            if not item.type in self.unwantedItemTypes:
                items.append(item)
        
        return items
    
    def getFolderListing(self, folderId):
        items = []
        
        for item in self.api.get_items(parent_id=folderId, limit=50, orderby="name_asc"):
            if not item.type in self.unwantedItemTypes:
                items.append(item)
        
        return items