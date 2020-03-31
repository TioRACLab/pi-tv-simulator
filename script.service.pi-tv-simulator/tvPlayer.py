"""
Manager the player of TV Simulator
"""

import os
import time
import xbmc
import xbmcaddon
import random

playlist = None

def findChannelFiles(folder):
    """Find all media files inner folder"""
    files = []
    
    for r, d, f in os.walk(folder):
        for file in f:
            files.append(os.path.join(r, file))
    
    return files

def start(folder, enableCommercials = False):
    """Start play channel media from media directory"""
    global playlist
    xbmc.executebuiltin("Playlist.Clear")
    time.sleep(0.5)
    videos = findChannelFiles(folder)
    random.shuffle(videos)
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

    if (enableCommercials):
        commercialsFolder = xbmcaddon.Addon("script.service.pi-tv-simulator").getSetting('commercialsFolder')
        commercials = findChannelFiles(commercialsFolder)
        random.shuffle(commercials)
        for video in videos:
            playlist.add(url=video)
            if (len(commercials) > 0):
                playlist.add(url=commercials[random.randint(0, len(commercials) - 1)])
    else:
        for video in videos:
            playlist.add(url=video)

    xbmc.Player().play(playlist)
    xbmc.executebuiltin("PlayerControl(RepeatAll)")

def startNoSignal():
    """Play channel without signal"""
    global playlist
    noSignalVideo = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), "resources", "background.mp4")
    xbmc.executebuiltin("Playlist.Clear")
    time.sleep(0.5)
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.add(url=noSignalVideo)
    xbmc.Player().play(playlist)
    xbmc.executebuiltin("PlayerControl(RepeatAll)")