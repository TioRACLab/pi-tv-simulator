"""
Service AddOn Kodi plugin. Start TV Simulator and manager external controls
"""

import os
import time
import xbmc
import xbmcaddon


def startAddon():
    """Start Pi TV Simulator AddOn"""
    start = xbmcaddon.Addon("script.service.pi-tv-simulator").getSettingBool('start')
    xbmc.log(msg='Loading TV - Start TV simulator? ' + str(start), level=xbmc.LOGDEBUG)

    if (start):
        xbmc.executebuiltin('XBMC.RunAddon(script.service.pi-tv-simulator)')
    
    pass


if __name__ == '__main__':
    
    startAddon()
    monitor = xbmc.Monitor()
    
    while not monitor.abortRequested():
        if monitor.waitForAbort(10):
            break

    #Testing
    #aquivo = "D:\\Code\\pi-tv-simulator\\script.service.pi-tv-simulator\\resources\\background.mp4"
    #playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    #playlist.add(url=aquivo)
    #xbmc.Player().play(playlist)
    #xbmc.executebuiltin("PlayerControl(RepeatAll)")

    # Sleep/wait for abort for 10 seconds
    