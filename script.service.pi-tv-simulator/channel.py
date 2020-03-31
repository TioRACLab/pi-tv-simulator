"""Manager channels"""

import xbmc
import tvPlayer
import xbmcaddon

channels = []
currentNumberChannel = 0
currentChannel = None

class Channel(object):
    """Class of a channel object"""
    
    def __init__(self, number = 0, directory = "", commercials = True):
        """Create instance, with number channel and media directory"""
        object.__init__(self)
        self.number = number
        self.directory = directory
        self.commercials = commercials

    def play(self):
        """Play channel"""
        tvPlayer.start(self.directory, self.commercials)


def loadAllChannels():
    """Load all channels from settings"""
    global channels

    for x in range(1, 5):
        enable = xbmcaddon.Addon("script.service.pi-tv-simulator").getSettingBool('channel' + str(x) + 'Enabled')

        if (enable):
            number = xbmcaddon.Addon("script.service.pi-tv-simulator").getSettingInt('channel' + str(x) + 'Number')
            directory = xbmcaddon.Addon("script.service.pi-tv-simulator").getSetting('channel' + str(x) + 'Folder')
            commercials = xbmcaddon.Addon("script.service.pi-tv-simulator").getSetting('channel' + str(x) + 'Commercials')
            channel = Channel(number, directory, commercials)
            channels.append(channel)
    
    channels.sort(key=lambda c: c.number)

def changeCurrentChannel(number):
    """Change channel by number"""
    global channels, currentChannel, currentNumberChannel
    currentNumberChannel = number
    xbmcaddon.Addon("script.service.pi-tv-simulator").setSettingInt('lastChannel', int(number))

    for channel in channels:
        if (channel.number == number):
            xbmc.log(msg='New Channel: ' + str(number), level=xbmc.LOGDEBUG)
            currentChannel = channel
            currentChannel.play()
            return currentChannel

    currentChannel = None
    tvPlayer.startNoSignal()
    return None

def loadLastChannel():
    """Load last channel from settings"""
    number = xbmcaddon.Addon("script.service.pi-tv-simulator").getSettingInt('lastChannel')
    channel = changeCurrentChannel(number)

    if (channel != None):
        channel.play()

    return channel

def upChannel():
    """Go up to the next valid channel"""
    for channel in channels:
        if (channel.number > currentNumberChannel):
            return changeCurrentChannel(channel.number)

    if (len(channels) > 0):
        return changeCurrentChannel(channels[0].number)
    else:
        return changeCurrentChannel(currentNumberChannel + 1)

def downChannel():
    """Go down to the next valid channel"""
    x = len(channels) - 1
    while(x >= 0):
        channel = channels[x]
        if (channel.number < currentNumberChannel):
            return changeCurrentChannel(channel.number)
        x = x - 1

    if (len(channels) > 0):
        return changeCurrentChannel(channels[-1].number)
    else:
        return changeCurrentChannel(currentNumberChannel + 1)