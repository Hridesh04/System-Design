from typing import List
from abc import ABC, abstractmethod

class Song:
    def __init__(self, title):
        self.__title = title

    def get_title(self):
        return self.__title
    
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Song:
        pass

class PlaylistIterator(Iterator):
    def __init__(self, song_list: List[Song]):
        self.__song_list = song_list
        self.__position = 0

    def has_next(self) -> bool:
        if self.__position < len(self.__song_list):
            return True
        else:
            return False

    def next(self) -> Song | None:
        while self.has_next() == True:
            song = self.__song_list[self.__position]
            self.__position += 1
            return song
        return None
    
class Playlist:
    def __init__(self):
        self.__playlist: List[Song] = []

    def add_song(self, song: Song):
        self.__playlist.append(song)

    def create_iterator(self) -> PlaylistIterator:
        return PlaylistIterator(self.__playlist)
    

playlist = Playlist()
playlist.add_song(Song("Song 1"))
playlist.add_song(Song("Song 2"))
playlist.add_song(Song("Song 3"))
playlist.add_song(Song("Song 4"))

iterator = playlist.create_iterator()
while iterator.has_next() == True:
    song = iterator.next()
    if song is not None:
        print(song.get_title())


