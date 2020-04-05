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
    #monitor = xbmc.Monitor()
    
    #while not monitor.abortRequested():
    #    if monitor.waitForAbort(10):
    #        break