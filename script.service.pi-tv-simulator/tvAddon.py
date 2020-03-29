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



#xbmc.executebuiltin('XBMC.RunScript(Q:\Scripts\myscript.py)')

channel.loadAllChannels()
channel.loadLastChannel()
tvSimulatorWindow.startWindow()