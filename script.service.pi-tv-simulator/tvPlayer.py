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
    files = []
    #xbmc.log(msg='Teste no outro.', level=xbmc.LOGDEBUG);

    # r=root, d=directories, f = files
    for r, d, f in os.walk(folder):
        for file in f:
            files.append(os.path.join(r, file))
    
    return files

def start(folder):
    global playlist
    xbmc.executebuiltin("Playlist.Clear")
    time.sleep(0.5)
    videos = findChannelFiles(folder)
    random.shuffle(videos)
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

    for video in videos:
        playlist.add(url=video)

    xbmc.Player().play(playlist)
    xbmc.executebuiltin("PlayerControl(RepeatAll)")

def startNoSignal():
    global playlist
    noSignalVideo = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), "resources", "background.mp4")
    xbmc.executebuiltin("Playlist.Clear")
    time.sleep(0.5)
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.add(url=noSignalVideo)
    xbmc.Player().play(playlist)
    xbmc.executebuiltin("PlayerControl(RepeatAll)")