from tkinter import *
from tkinter import filedialog
import MusicPlayer as mp
from UIConstants import UIConstants as ui

# https://docs.python.org/3/library/tkinter.html#how-to-use-this-section
class App(Frame):
    '''
    The app class handles the front end interface with the user and also calls to backend music
    handling.
    '''
    def __init__(self, source, master=None):
        '''
        A constructor that takes in a Tk() master object (optional, defaults to None)
        Initializes the UI for the Tk window object.
        '''
        super().__init__(master)
        self.pack(expand=True, fill=BOTH)

        self.musicPlayer = mp.MusicPlayer()
        # self.musicPlayer.readMusicFile("defaults")

        # set up UI frames
        self.playBackFrame = Frame(self, bg=ui.fgLight)
        self.playBackFrame.pack(side=TOP, fill=X, ipady=ui.padSmall)
        self.playListsFrame = Frame(self, bg=ui.bgLight)
        self.playListsFrame.pack(side=LEFT, fill=Y)
        self.songFrame = Frame(self, bg=ui.bgDark)
        self.songFrame.pack(expand=True, fill=BOTH)

        # playBackFrame UI
        self.rewindButton = Button(self.playBackFrame, text="<<")
        self.rewindButton.pack(side=LEFT, padx=(ui.padSmall, ui.padNone))
        self.playButton = Button(self.playBackFrame, text=">")
        self.playButton.pack(side=LEFT)
        self.fastForwardButton = Button(self.playBackFrame, text=">>")
        self.fastForwardButton.pack(side=LEFT)

        self.songScaleValue = self.musicPlayer.getVolumeVar()
        self.songScale = Scale(self.playBackFrame, orient=HORIZONTAL,
                variable=self.songScaleValue)
        self.songScale.pack(side=LEFT, padx=(ui.padSmall, ui.padNone))

        # songFrame UI
        self.songListBox = Listbox(self.songFrame, selectmode=SINGLE)
        self.songListBox.pack(expand=True, fill=BOTH)

    def helloCallBack(self):
        pass
        # self.songListBox.delete(1)
        # self.songListBox.insert(1, self.getSongScaleValue())
        # print(self.songListBox.get(0))
        # print(self.songListBox.get(1))

    def getSongScaleValue(self):
        return self.songScaleValue.get()

    def get_songs(self, source_directory):
        if source_directory is None:
            raise TypeError("Cannot give NoneType source_directory")
