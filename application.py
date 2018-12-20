from tkinter import *
import musicplayer as mp
from uiconstants import UIConstants as ui

# https://docs.python.org/3/library/tkinter.html#how-to-use-this-section
class App(Frame):
    '''
    The app class handles the front end interface with the user and also calls to backend music
    handling.
    '''
    def __init__(self, master=None):
        '''
        A constructor that takes in a Tk() master object (optional, defaults to None)
        Initializes the UI for the Tk window object.
        '''
        super().__init__(master)
        self.pack(expand=True, fill=BOTH)

        self.musicPlayer = mp.MusicPlayer()
        # self.musicPlayer.readMusicFile("defaults")

        self.playBackFrame = Frame(self, bg=ui.fgLight)
        self.playBackFrame.pack(side=TOP, fill=X)

        self.playListsFrame = Frame(self, bg=ui.bgLight)
        self.playListsFrame.pack(side=LEFT, fill=Y)

        self.songsFrame = Frame(self, bg=ui.bgDark)
        self.songsFrame.pack(expand=True, fill=BOTH)

        self.image = PhotoImage(file="./img/jukebox.png")
        self.testButton = Button(self.playListsFrame, text="Test",
                command=self.helloCallBack)
        self.testButton.config(image=self.image, width=100, height=100)
        self.testButton.pack(side=LEFT)

        # playBackFrame UI
        self.rewindButton = Button(self.playBackFrame, text="<<")
        self.rewindButton.pack(side=LEFT)
        self.playButton = Button(self.playBackFrame, text=">")
        self.playButton.pack(side=LEFT)
        self.fastForwardButton = Button(self.playBackFrame, text=">>")
        self.fastForwardButton.pack(side=LEFT)
        self.songScaleValue = DoubleVar()
        self.songScale = Scale(self.playBackFrame, variable=self.songScaleValue)
        self.songScale.pack()

        self.songLabel = Label(self.songsFrame, text="ImaSong")
        self.songLabel.pack()

    def helloCallBack(self):
        self.songLabel["text"] = self.getSongScaleValue()

    def getSongScaleValue(self):
        return self.songScaleValue.get()
