# import the needed files
import pygame
from tkinter import *
from music_player import MusicPlayer

# create a class PlaySong that inherits from the class MusicPlayer
class PlaySong(MusicPlayer):
    
    def set_status(self):
        # Displaying Status
        self.status.set("-Playing")