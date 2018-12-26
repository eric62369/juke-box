import os
import six

class Playlist():
    # Playlist constants. DO NOT MODIFY
    playlist_directory = "playlists"
    playlist_header = "#EXTM3U"
    playlist_song_header = "#EXTINF:,"
    playlist_song_prefix = ".."

    def __init__(self, filepath=None, name="default"):
        '''
            pre: takes in a String filepath and a String name
                default name is "default", default filepath is None
            post: Initializes either an existing or new playlist object
        '''
        self.songs = []
        self.filepath = None
        if filepath is None:  # new playlist
            self.filepath = name + ".m3u"
        else:  # existing playlist
            # self.name = filepath
            pass

    def add(self, songlist=None, filepath=None):
        '''
            Songlist is Not None:
            pre: Takes in a list of songs as songlist and a filepath for the directory containing
                songlist.
                if songlist or filepath is None, raises TypeError
            post: Adds the given filepath song(s) to the playlist
            Songlist is None:
            pre: Takes in a String filepath that can be a directory of songs or an individual song.
                directories of songs are added in sorted order
                if the filepath does not exist, raises IOError
                if the filepath is None, raises TypeError
            post: Adds the given filepath song(s) to the playlist
        '''
        if filepath is None:
            raise TypeError("Cannot give a NoneType filepath")
        if songlist is None:
            if not os.path.exists(filepath):
                raise IOError("The given filepath '" + filepath + "' is invalid")
            if os.path.isdir(filepath):  # Do recursive add for all songs in dir and sub-dirs
                files = os.listdir(filepath)
                for file in sorted(files):
                    file = os.path.join(filepath, file)
                    self.add(filepath=file)
            else:  # Add the one song
                self.songs.append(filepath)
        else:
            for song in songlist:
                path = os.path.join(filepath, song)
                if os.path.exists(path):
                    self.songs.append(path)

    def remove(self, songs):
        '''
            pre: Takes in a String song, which is a filepath to the song in the playlist object.
                if the song is None, raises TypeError
            post: Removes the given song from the playlist. Currently runs in O(N) time
            pre: Takes in a list of songs.
                if songs is None or any song in songs is None, raises TypeError
            post: Removes the given list of songs from the playlist object. Currently runs in
                O(N^2) time
        '''
        if songs is None:
            raise TypeError("Given song(s) cannot be None")
        if isinstance(songs, six.string_types):
            try:
                print(songs)
                print(self.songs)
                self.songs.remove(songs)
            except:
                raise
        else:
            for song in songs:
                try:
                    self.songs.remove(song)
                except:
                    raise

    def remove_duplicates(self):
        '''
            post: takes the current list of songs and removes all duplicates from the list of songs.
        '''
        no_dupes = set(self.songs)
        self.songs = []
        for unique in sorted(no_dupes):
            self.songs.append(unique)

    def save(self):
        '''
            post: Writes the current set of songs in the playlist to the designated location
                in the file system in a playlists/ directory. IO operations may fail.
                Will prepend a prefix (../) for navigating one directory back outside of the
                playlists directory
        '''
        # TODO: needs some tweaking for existing playlists
        target_path = os.path.join(Playlist.playlist_directory, self.filepath)
        if not os.path.exists(Playlist.playlist_directory):
            os.mkdir(Playlist.playlist_directory)
        with open(target_path, 'w') as file:
            file.write(Playlist.playlist_header + "\n")
            for song in self.songs:
                file.write(Playlist.playlist_song_header + "\n")
                song = os.path.join(Playlist.playlist_song_prefix, song)
                file.write(song + "\n")
        return True

    def __str__(self):
        '''
            post: An override for the __str__ function. Prints out the playlist filepath and song
                contents
        '''
        return "Playlist:" + self.filepath + ":: " + str(self.songs)

if __name__ == "__main__":
    playlist = Playlist()
    def test_remove(isList=False):
        path = os.path.join("Jukebox Material", "Deltarune Chapter 1 OST")
        songs = test_add_songlist()
        if isList:
            for i in range(len(songs)):
                songs[i] = os.path.join(path, songs[i])
            playlist.remove(songs)
        else:
            song = os.path.join(path, songs[0])
            playlist.remove(song)
        playlist.save()

    def test_add_songlist():
        path = os.path.join("Jukebox Material", "Deltarune Chapter 1 OST")
        songs = os.listdir(path)
        songs = [songs[0], songs[1], songs[2]]
        playlist.add(songs, path)
        playlist.save()
        return songs

    def test_remove_dupes():
        playlist.add(filepath="Jukebox Material/Deltarune Chapter 1 OST")
        playlist.add(filepath="Jukebox Material/Deltarune Chapter 1 OST")
        playlist.remove_duplicates()
        playlist.save()
    test_remove(False)
    # test_remove_dupes()
