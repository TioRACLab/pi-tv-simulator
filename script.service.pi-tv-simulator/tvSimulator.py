import os
import time
import xbmc
import xbmcaddon
import random
import outro

playlist = None

if __name__ == '__main__':
    monitor = xbmc.Monitor()
    
    while not monitor.abortRequested():

        if (playlist == None):
            videos = outro.findChannelFiles()
            random.shuffle(videos)
            playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

            for video in videos:
                playlist.add(url=video)

            xbmc.Player().play(playlist)
            xbmc.executebuiltin("PlayerControl(RepeatAll)")

        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break