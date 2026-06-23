from typing import List

class Song:
    def __init__(self, title):
        self.__title = title

    def get_title(self):
        return self.__title
    
class Playlist:
    def __init__(self):
        self.__playlist: List[Song] = []

    def add_song(self, song: Song):
        self.__playlist.append(song)

    def get_playlist(self):
        return self.__playlist
    
playlist = Playlist()
song1 = Song("Song 1")
song2 = Song("Song 2")
song3 = Song("Song 3")
song4 = Song("Song 4")
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)
playlist.add_song(song4)

for song in playlist.get_playlist():
    print(song.get_title())
