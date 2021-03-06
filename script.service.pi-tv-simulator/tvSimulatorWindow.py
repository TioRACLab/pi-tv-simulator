import os
import xbmc
import xbmcgui
import xbmcaddon
import channel

#import tvInterfaceControl

currentWindow = None

class TvSimulatorWindow(xbmcgui.WindowXMLDialog):
    """TV Simulator AddOn Window"""

    def __init__(self, *args, **kwargs):
        """Create instance"""
        self.addon = xbmcaddon.Addon()
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

        #self.group = xbmcgui.ControlGroup(0, 0, self.getWidth(), self.getHeight())
        #self.label1 = xbmcgui.ControlLabel(self.getWidth() - 200, 30, 200, 900, '01', textColor ='0xFF00FF00', font="WeatherTemp")

    def onInit(self):
        """On init, create controls"""
        self.group = self.getControl(15001)
        self.group.setWidth(self.getWidth())
        self.group.setHeight(self.getHeight())

        self.labelNumber = self.getControl(15002)
        self.labelNumber.setPosition(self.getWidth() - 200, 30)
        #self.tvInterface = tvInterfaceControl.TvInterfaceControl(self)
        #self.tvInterface.start()
        self.changeChannelNumber()
        self.changeLabelChannel("69")

    def onAction(self, action):
        """Get keyboard interaction"""
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
        elif (code == 61569):
            xbmc.log(msg='Down Channel', level=xbmc.LOGDEBUG)
            channel.downChannel()
            self.changeChannelNumber()
        elif (code == 61467):
            self.close()
        '''elif (code == 61552):
            self.tvInterface.addCharSelection("0")
        elif (code == 61553):
            self.tvInterface.addCharSelection("1")
        elif (code == 61554):
            self.tvInterface.addCharSelection("2")
        elif (code == 61555):
            self.tvInterface.addCharSelection("3")
        elif (code == 61556):
            self.tvInterface.addCharSelection("4")
        elif (code == 61557):
            self.tvInterface.addCharSelection("5")
        elif (code == 61558):
            self.tvInterface.addCharSelection("6")
        elif (code == 61559):
            self.tvInterface.addCharSelection("7")
        elif (code == 61560):
            self.tvInterface.addCharSelection("8")
        elif (code == 61561):
            self.tvInterface.addCharSelection("9")'''
        


        key = None if code == 0 else str(code)
        xbmc.log(msg='BottunCode??? ' + str(key), level=xbmc.LOGDEBUG)

    def close(self):
        """Close window"""
        xbmc.log(msg='Close TV!', level=xbmc.LOGDEBUG)
        #self.tvInterface.stop()
        #self.tvInterface = None
        xbmcgui.WindowXMLDialog.close(self)
        
    def changeChannelNumber(self):
        xbmc.log(msg='Change Channel Number', level=xbmc.LOGDEBUG)
        #self.tvInterface.addChannel(channel.currentNumberChannel)

    def changeLabelChannel(self, text):
        xbmc.log(msg='Change Label Number: ' + str(text), level=xbmc.LOGDEBUG)
        self.labelNumber.setLabel(str(text))

def startWindow():
    """Create Window and open"""
    global currentWindow
    currentWindow = TvSimulatorWindow("tvSimulator.xml", xbmcaddon.Addon("script.service.pi-tv-simulator").getAddonInfo('path'), 'default', '1080i')
    currentWindow.doModal()

def getWindow():
    """Return current Window"""
    global currentWindow
    return currentWindow
        