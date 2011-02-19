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

import xbmcaddon as xa

import putio

class PutIO(object):
    """
    Class to handle putio api calls for XBMC actions
    
    """
    
    wantedItemTypes = ("folder", "movie", "audio", "unknown", "file")
    subtitleTypes = ("srt", "sub")
    
    def __init__(self):
        self.addon = xa.Addon(os.path.basename(os.getcwd()))
        self.api_key = self.addon.getSetting("api_key")
        self.api_secret = self.addon.getSetting("api_secret")
        self.api = putio.Api(self.api_key, self.api_secret)
    
    def getItem(self, itemId):
        return self.api.get_items(id=itemId)[0]
    
    def getRootListing(self):
        items = []
        
        for item in self.api.get_items(limit=1000):
            if item.type in self.wantedItemTypes:
                items.append(item)
        
        return items
    
    def getFolderListing(self, folderId):
        items = []
        
        for item in self.api.get_items(parent_id=folderId, limit=1000, orderby="name_asc"):
            if item.type in self.wantedItemTypes:
                items.append(item)
        
        return items
    
    def getSubtitle(self, item):
        fileName, extension = os.path.splitext(item.name)
        
        for i in self.getFolderListing(item.parent_id):
            if i.type != "folder":
                fn, ext = os.path.splitext(i.name)
                
                xbmc.log("SEARCHING FOR %s IN %s" % (fileName, i.name))
                
                if i.name.find(fileName) != -1 and (ext.lstrip(".") in self.subtitleTypes):
                    xbmc.log("FOUND SUBTITLE AT: %s" % i.get_stream_url())
                    return i.get_stream_url()