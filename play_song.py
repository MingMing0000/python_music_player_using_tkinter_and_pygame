# import the needed files
import pygame
from tkinter import *
from music_controls import MusicControls

# create a class PlaySong that inherits from the class MusicPlayer
class PlaySong(MusicControls):
    def __init__(self, player):
        self.player = player
        self.status = player.status
        self.track = player.track
    
    def set_status(self):
        # Displaying Status
        self.status.set("-Playing")

    def play_song(self):
        # Displaying Selected Song title
        self.track.set(self.player.playlist.get(ACTIVE))
        # Loading Selected Song
        pygame.mixer.music.load(self.player.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()