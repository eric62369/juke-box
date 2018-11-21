
class MusicPlayer():
    def __init__(self, filePath="defaultLibrary.txt"):
        '''
        Takes in a String filePath representing an absolute file path
        to a file containing paths to all music in the user's library
        '''
        with open(filePath, 'r') as library:
            self.songList = library.read().splitlines()
            self.songSet = set(self.songList)

    def readMusicFile(self, filePath):
        '''
        Takes in a String filePath representing the absolute file path
        to a music file
        '''
        if filePath in self.songSet:
            # TODO: Read the music file
            pass
