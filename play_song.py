# import the needed files
import pygame
from tkinter import *
from music_player import MusicPlayer

# create a class PlaySong that inherits from the class MusicPlayer
class PlaySong(MusicPlayer):
    
    def set_status(self):
        # Displaying Status
        self.status.set("-Playing")

    def play_song(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()