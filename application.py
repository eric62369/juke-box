import tkinter as tk
from tkinter import Button, Frame
import musicplayer as mp

# https://docs.python.org/3/library/tkinter.html#how-to-use-this-section
class App(tk.Frame):
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
        self.pack(expand=True, fill="both")

        self.musicPlayer = mp.MusicPlayer()
        # self.musicPlayer.readMusicFile("defaults")

        self.playbackFrame = tk.Frame(self, bg="blue")
        self.playbackFrame.pack(side="top", fill="x")

        self.playListsFrame = tk.Frame(self, bg="red")
        self.playListsFrame.pack(side="left", fill="y")

        self.testButton = tk.Button(self.playListsFrame, text="Test", bg="red", command=self.helloCallBack)
        self.testButton.pack(side="left")

        self.testLabel = tk.Label(self.playbackFrame, text="Yahs", relief=tk.RAISED)
        self.testLabel.pack(side="left")

    def helloCallBack(self):
        self.testLabel["text"] = "Super yahs"
