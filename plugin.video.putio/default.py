# coding: utf-8

import sys

import xbmcgui
import xbmcplugin

thisPlugin = int(sys.argv[1])

def createListing():
    return [
        "first item",
        "second item",
        "third item"
    ]

def sendToXbmc(listing):
    global thisPlugin
    
    for item in listing:
        listItem = xbmcgui.ListItem(item)
        xbmcplugin.addDirectoryItem(thisPlugin, "", listItem)
    
    xbmcplugin.endOfDirectory(thisPlugin)

sendToXbmc(createListing())