import xbmcplugin as xp

import putio

class PutIO(object):
    """
    Class to handle putio api calls for XBMC actions
    
    """
    
    def __init__(self, pluginId):
        self.api_key = xp.getSetting(pluginId, "api_key")
        self.api_secret = xp.getSetting(pluginId, "api_secret")
        self.api = putio.Api(self.api_key, self.api_secret)
    
    def getRootListing(self):
        return [f for f in self.api.get_items()]
    
    def getFolderListing(self, folderId):
        return [f for f in self.api.get_items(parent_id=folderId)]