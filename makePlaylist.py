import os

class Playlist():
    def __init__(self, filepath=None, name="default"):
        '''
            pre: takes in a String filepath and a String name

            post: Initializes either an existing or new playlist object
        '''
        self.songs = []
        self.name = name
        self.filepath = filepath
        if filepath is None:  # new playlist
            self.filepath = self.name + ".m3u"
        else:  # existing playlist
            # self.name = filepath
            pass

    def add(self, filepath):
        if not os.path.exists(filepath):
            raise IOError("The given filepath '" + filepath + "' is invalid")
        if os.path.isdir(filepath):  # Do recursive add for all songs in dir and sub-dirs
            files = os.path.listdir(filepath)
            for file in files:
                print(file)
                add(file)
        else:  # Add the one song
            self.songs.append(filepath)

    def save():
        pass

    def __str__(self):
        return "Playlist:" + self.filepath + ":: " + str(self.songs)

if __name__ == "__main__":
    playlist = Playlist()
    print(playlist)
    playlist.add("a")
