"""
AddOn starting
"""

import os
import time
import xbmc
import xbmcgui
import xbmcaddon
import random
import tvPlayer

class TestWindow(xbmcgui.WindowDialog):
    def __init__(self):
        #
        self.label1 = xbmcgui.ControlLabel(self.getWidth() - 200, 30, 200, 900, '01', textColor ='0xFF00FF00', font="WeatherTemp")
        self.addControl(self.label1)


tvPlayer.start()
window = TestWindow()
window.doModal()


