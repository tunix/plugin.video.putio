# coding: utf-8
#
# put.io xbmc addon
# Copyright (C) 2009  Alper Kanat <tunix@raptiye.org>
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

import putio
import xbmcaddon as xa
from exceptions import PutioAuthFailureException


class PutioApiHandler(object):
    """
    Class to handle putio api calls for XBMC actions

    """

    subtitleTypes = ("srt", "sub")

    def __init__(self, pluginId):
        self.addon = xa.Addon(pluginId)
        self.oauthkey = self.addon.getSetting("oauthkey").replace('-', '')

        if not self.oauthkey:
            raise PutioAuthFailureException(
                self.addon.getLocalizedString(30001),
                self.addon.getLocalizedString(30002)
            )

        self.apiclient = putio.Client(self.oauthkey)

    def getItem(self, itemId):
        return self.apiclient.File.GET(itemId)

    def getRootListing(self):
        items = []

        for item in self.apiclient.File.list(parent_id=0):
            items.append(item)

        return items

    def getFolderListing(self, folderId, isItemFilterActive=True):
        items = []

        for item in self.apiclient.File.list(parent_id=folderId):
            if isItemFilterActive:
                continue

            items.append(item)

        return items

    def getSubtitle(self, item):
        fileName, extension = os.path.splitext(item.name)

        for i in self.getFolderListing(item.parent_id, False):
            if i.type != "folder":
                fn, ext = os.path.splitext(i.name)

                if i.name.find(fileName) != -1 and (ext.lstrip(".") in self.subtitleTypes):
                    return i.get_stream_url()
