"""TV interface control"""

import time
import xbmc
import channel
import threading
from datetime import datetime

class TvInterfaceControl(threading.Thread):
    
    def __init__(self, tvWindow):
        threading.Thread.__init__(self)
        self.tvWindow = tvWindow
        self.selection = None
        self.dateStartSelection = None
        self.selected = False
        self._stop = False

    def run(self):
        while not self._stop:
            if (self.selection != None):
                diff = datetime.now() - self.dateStartSelection
                if (diff.seconds >= 5):
                    if (self.selected):
                        self.hideSelecion()
                    else:
                        channel.changeCurrentChannel(self.selection)
                        self.addChannel(self.selection)
            time.sleep(0.5)

    def addChannel(self, channel):
        self.selection = str(channel).zfill(2)
        self.dateStartSelection = datetime.now()
        self.selected = True
        self.showSelection()

    def addCharSelection(self, char):
        if (self.selection == None or len(self.selection) == 2):
            self.selection = str(char)
        else:
            self.selection += str(char)
        
        self.selected = False
        self.dateStartSelection = datetime.now()
        self.showSelection()

    def showSelection(self):
        labelText = ""

        if (self.selected):
            labelText = str(self.selection).ljust(2, '0')
        else:
            labelText = str(self.selection).rjust(2, "-")
            

        self.tvWindow.changeLabelChannel(labelText)

    def hideSelecion(self):
        self.tvWindow.changeLabelChannel("")
        self.selection = None
        self.dateStartSelection = None
        self.selected = False

    def stop(self):
        self._stop = True