"""TV interface control"""

import time
import xbmc
import channel
import threading
from datetime import datetime

class TvInterfaceControl(threading.Thread):
    """Class manager interface control"""
    
    def __init__(self, tvWindow):
        """Create interface control"""
        threading.Thread.__init__(self)
        self.tvWindow = tvWindow
        self.selection = None
        self.dateStartSelection = None
        self.selected = False
        self._stop = False

    def run(self):
        """Process looping"""
        while not self._stop:
            self.processSelectionChannel()
            time.sleep(0.5)

    #Manager selection channel

    def processSelectionChannel(self):
        """Show or hide selection channel"""
        if (self.selection != None):
                diff = datetime.now() - self.dateStartSelection
                if (diff.seconds >= 5):
                    if (self.selected):
                        self.hideSelecion()
                    else:
                        channel.changeCurrentChannel(self.selection)
                        self.addChannel(self.selection)

    def addChannel(self, channel):
        """Change number channel"""
        self.selection = str(channel).zfill(2)
        self.dateStartSelection = datetime.now()
        self.selected = True
        self.showSelection()

    def addCharSelection(self, char):
        """Select one char and wait new selection"""
        if (self.selection == None or len(self.selection) == 2):
            self.selection = str(char)
        else:
            self.selection += str(char)
        
        self.selected = False
        self.dateStartSelection = datetime.now()
        self.showSelection()

    def showSelection(self):
        """Show current selection"""
        labelText = ""

        if (self.selected):
            labelText = str(self.selection).ljust(2, '0')
        else:
            labelText = str(self.selection).rjust(2, "-")
            

        self.tvWindow.changeLabelChannel(labelText)

    def hideSelecion(self):
        """Hide current selection and clear"""
        self.tvWindow.changeLabelChannel("")
        self.selection = None
        self.dateStartSelection = None
        self.selected = False

    #End manager selection channel

    def stop(self):
        """Stop manager control"""
        self._stop = True