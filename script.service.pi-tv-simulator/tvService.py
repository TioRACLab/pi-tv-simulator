import os
import time
import xbmc
import xbmcaddon
import random
import outro

if __name__ == '__main__':
    monitor = xbmc.Monitor()
    start = xbmcaddon.Addon("script.service.pi-tv-simulator").getSetting('start')
    xbmc.log(msg='Teste no outro: ' + str(start), level=xbmc.LOGDEBUG);
    
    while not monitor.abortRequested():

        if (start == 'true'):
            #outro.start()
            #xbmc.executebuiltin('XBMC.RunAddon(script.service.pi-tv-simulator)')
            aquivo = "D:\\Code\\pi-tv-simulator\\script.service.pi-tv-simulator\\resources\\background.mp4"
            playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            playlist.add(url=aquivo)
            xbmc.Player().play(playlist)
            xbmc.executebuiltin("PlayerControl(RepeatAll)")
            start = False

        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break