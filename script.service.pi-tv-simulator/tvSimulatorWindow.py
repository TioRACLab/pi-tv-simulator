import os
import xbmc
import xbmcgui
import xbmcaddon

import channel

currentWindow = None

class TvSimulatorWindow(xbmcgui.WindowXMLDialog):
    """Principal AddOn window"""

    def __init__(self, *args, **kwargs):
        self.addon = xbmcaddon.Addon()
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

        #self.group = xbmcgui.ControlGroup(0, 0, self.getWidth(), self.getHeight())
        #self.label1 = xbmcgui.ControlLabel(self.getWidth() - 200, 30, 200, 900, '01', textColor ='0xFF00FF00', font="WeatherTemp")

    def onInit(self):
        self.group = self.getControl(15001)
        self.group.setWidth(self.getWidth())
        self.group.setHeight(self.getHeight())

        self.labelNumber = self.getControl(15002)
        self.labelNumber.setPosition(self.getWidth() - 200, 30)
        self.changeChannelNumber()

    def onAction(self, action):
        code = action.getButtonCode()
        #61568 - Cima
        #61569 - Baixo
        #61570 - Esquerda
        #61571 - Direita
        #61553 - 1
        #61554 - 2
        #61555 - 3
        #61556 - 4
        #61557 - 5
        #61558 - 6
        #61559 - 7
        #61560 - 8
        #61561 - 9
        #61552 - 0

        if (code == 61568):
            xbmc.log(msg='Up Channel', level=xbmc.LOGDEBUG)
            channel.upChannel()
            self.changeChannelNumber()

        if (code == 61569):
            xbmc.log(msg='Down Channel', level=xbmc.LOGDEBUG)
            channel.downChannel()
            self.changeChannelNumber()
        
        if (code == 61467):
            self.close()


        key = None if code == 0 else str(code)
        xbmc.log(msg='BottunCode??? ' + str(key), level=xbmc.LOGDEBUG)

    def close(self):
        xbmc.log(msg='Close TV!', level=xbmc.LOGDEBUG)
        xbmcgui.WindowXMLDialog.close(self)
        
    def changeChannelNumber(self):
        self.labelNumber.setLabel(str(channel.currentNumberChannel).zfill(2))

'''
class ThreadTvWindow(threading.Thread):
    """Thread for control to TV Simulator Window"""
    
    def __init__(self):
        """Create Thread Class"""
        threading.Thread.__init__(self)
        self._window = TvSimulatorWindow()

    def run(self):
        """Open Tv Simulator Window"""
        self._window.doModal()

    def getWindow(self):
        """Return current Window"""
        return self._window
'''

def startWindow():
    """Create Window and open"""
    global currentWindow
    currentWindow = TvSimulatorWindow("tvSimulator.xml", xbmcaddon.Addon().getAddonInfo('path'), 'default', '1080i')
    currentWindow.doModal()

def getWindow():
    """Return current Window"""
    global currentWindow
    return currentWindow
        