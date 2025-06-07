# import the files needed
import pygame
from music_controls import MusicControls
from tkinter import *

# create a class PauseSong that inherits from the class MusicControls
class PauseSong(MusicControls):
    def __init__(self, player):
        self.player = player
        self.status = player.status    
    
    def set_status(self):
        self.status.set("-Paused")

    def pause_song(self):
        # Paused Song
        pygame.mixer.music.pause()