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
            outro.start()
            start = False

        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break