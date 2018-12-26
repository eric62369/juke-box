from tkinter import *
import os
# from pygame import mixer as mixer

class MusicPlayer():
    def __init__(self, filepath="defaultLibrary.txt"):
        '''
        Takes in a String filepath representing an absolute file path
        to a file containing paths to all music in the user's library
        '''
        self.songList = []
        self.songSet = set(self.songList)
        if os.path.exists(filepath):
            with open(filepath, 'r') as library:
                self.songList = library.read().splitlines()
                self.songSet = set(self.songList)

        self.volume = DoubleVar()
        self.isPlaying = False

        # mixer.init()
        # mixer.music.load("myFile.wav")
        # mixer.music.play()
        # while mixer.music.get_busy() == True:
        #     continue

    def readMusicFile(self, filepath):
        '''
        Takes in a String filepath representing the absolute file path
        to a music file
        '''
        if filepath in self.songSet:
            # TODO: Read the music file
            pass

    def getVolumeVar(self):
        return self.volume

    def getIsPlaying(self):
        return self.isPlaying

    def switchIsPlaying(self):
        self.isPlaying = not self.isPlaying
