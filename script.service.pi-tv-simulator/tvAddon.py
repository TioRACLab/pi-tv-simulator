"""
AddOn starting
"""

import os
import time
import xbmc
import random
import xbmcgui
import xbmcaddon
import channel
import tvSimulatorWindow


channel.loadAllChannels()
channel.loadLastChannel()
tvSimulatorWindow.startWindow()

#xbmc.executebuiltin("Playlist.Clear")
#time.sleep(0.5)
#xbmc.executebuiltin("PlayerControl(Stop)")
#xbmc.executebuiltin("XBMC.ActivateWindow(10000)")