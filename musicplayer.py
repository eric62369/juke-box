from tkinter import *
from pygame import mixer as mixer

class MusicPlayer():
    def __init__(self, filePath="defaultLibrary.txt"):
        '''
        Takes in a String filePath representing an absolute file path
        to a file containing paths to all music in the user's library
        '''
        with open(filePath, 'r') as library:
            self.songList = library.read().splitlines()
            self.songSet = set(self.songList)

        self.volume = DoubleVar()
        self.isPlaying = False

        # mixer.init()
        # mixer.music.load("myFile.wav")
        # mixer.music.play()
        # while mixer.music.get_busy() == True:
        #     continue

    def readMusicFile(self, filePath):
        '''
        Takes in a String filePath representing the absolute file path
        to a music file
        '''
        if filePath in self.songSet:
            # TODO: Read the music file
            pass

    def getVolumeVar(self):
        return self.volume

    def getIsPlaying(self):
        return self.isPlaying

    def switchIsPlaying(self):
        self.isPlaying = not self.isPlaying

import pygame
