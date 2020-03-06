"""
AddOn starting
"""

import os
import time
import xbmc
import random
import xbmcgui
import xbmcaddon
import lib.tvPlayer as tvPlayer
import lib.tvSimulatorWindow as tvSimulatorWindow



#xbmc.executebuiltin('XBMC.RunScript(Q:\Scripts\myscript.py)')
tvPlayer.start()
tvSimulatorWindow.startWindow()