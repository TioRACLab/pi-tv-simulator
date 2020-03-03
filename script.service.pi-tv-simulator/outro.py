import os
import time
import xbmc
import xbmcaddon
import random

playlist = None

def findChannelFiles():
    path =  xbmcaddon.Addon("script.service.pi-tv-simulator").getSetting('pastinha')
    files = []
    #xbmc.log(msg='Teste no outro.', level=xbmc.LOGDEBUG);

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    
    return files

def start():
    global playlist
    if (playlist == None):
        videos = findChannelFiles()
        random.shuffle(videos)
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

        for video in videos:
            playlist.add(url=video)

        xbmc.Player().play(playlist)
        xbmc.executebuiltin("PlayerControl(RepeatAll)")