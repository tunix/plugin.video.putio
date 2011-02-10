import xbmc
import xbmcgui as xg
import xbmcplugin as xp

iconMapping = {
    "folder": "DefaultFolder.png",
    "movie": "DefaultVideo.png",
    "audio": "DefaultAudio.png"
}

def getIcon(fileType):
    return iconMapping.get(fileType, "DefaultFile.png")

def populateDir(pluginUrl, pluginId, listing):
    for item in listing:
        if item.is_dir:
            url = "%s?%s" % (pluginUrl, item.id)
        else:
            url = item.get_stream_url()
        
        listItem = xg.ListItem(
            item.name,
            item.name,
            getIcon(item.type),
            getIcon(item.type)
        )
        
        xp.addDirectoryItem(
            pluginId,
            url,
            listItem,
            item.is_dir
        )
    
    xp.endOfDirectory(pluginId)