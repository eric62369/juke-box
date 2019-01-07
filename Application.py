from tkinter import *
from tkinter import filedialog
import os
import MusicPlayer as mp
from MakePlaylist import Playlist
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
            pre: Takes in a String source non-default argument. It is assumed to be a legal
                file directory, where a music library is stored on a device (i.e. mp3 player)
        '''
        super().__init__(master)
        self.pack(expand=True, fill=BOTH)

        self.source_directory = source
        self.musicPlayer = mp.MusicPlayer()
        # self.musicPlayer.readMusicFile("defaults")

        # set up UI frames
        self.playBackFrame = Frame(self, bg=ui.fgLight)
        self.playBackFrame.pack(side=TOP, fill=X, ipady=ui.padSmall)
        self.playListsFrame = Frame(self, bg=ui.bgLight)
        self.playListsFrame.pack(side=LEFT, fill=Y)
        self.songFrame = MainView(self, source=self.source_directory, bg=ui.bgDark)
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
        # self.songListBox = Listbox(self.songFrame, selectmode=SINGLE)
        # self.songListBox.pack(expand=True, fill=BOTH)

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

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class PlaylistPage(Page):
    def __init__(self, *args, **kwargs):
        self.source = None
        if "source" in kwargs:
            self.source = kwargs["source"]
            kwargs.pop("source")
        Page.__init__(self, *args, **kwargs)
        self.playlists = None
        self.playlists = self.read_in_playlists()
        self.instructions = Label(self, text="Create a new Playlist")
        self.instructions.pack(anchor=NW)
        self.name_input = Entry(self)
        self.name_input.pack(anchor=NW)
        self.create_button = Button(self,
                text="Create Playlist",
                command=lambda: self.create_playlist(name=self.name_input.get(),
                        source_directory=self.source))
        self.create_button.pack(anchor=NW)
        self.notification_label = Label(self, text="")
        self.notification_label.pack(anchor=NW)

    def playlist_created_notification(self, name):
        self.notification_label.config(text="Created playlist: " + name)

    def create_playlist(self, name, source_directory):
        if name == "":
            name = None
        playlist = Playlist(filepath=source_directory, name=name)
        playlist.add(filepath="Jukebox Material")
        playlist.save()
        self.playlists.append(playlist)
        self.playlist_created_notification(name + ".m3u")

    def read_in_playlists(self):
        directory_contents = []
        if os.path.exists(Playlist.playlist_directory):
            directory_contents = os.listdir(Playlist.playlist_directory)
        playlists = []
        for file in directory_contents:
            if Playlist.isFilePlaylist(file):
                playlists.append(file)
        return playlists

class AddSongPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="Add songs to playlists")
        label.pack(side=TOP, fill=BOTH, expand=True)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        self.source = None
        if "source" in kwargs:
            self.source = kwargs["source"]
            kwargs.pop("source")
        Frame.__init__(self, *args, **kwargs)
        p1 = PlaylistPage(self, source=self.source)
        p2 = AddSongPage(self)
        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = Button(buttonframe, text="Page 2", command=p2.lift)

        b1.pack(side="left")
        b2.pack(side="left")

        p1.show()
