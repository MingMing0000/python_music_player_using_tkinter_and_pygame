# import the files needed
import pygame
from music_controls import MusicControls
from tkinter import *

# create a class UnpauseSong that inherits from the class MusicControls
class UnpauseSong(MusicControls):
    def __init__(self, player):
        self.player = player
        self.status = player.status
    
    def set_status(self):
        # It will Display the  Status
        self.status.set("-Playing")

    def unpause_song(self):
        # Playing back Song
        pygame.mixer.music.unpause()