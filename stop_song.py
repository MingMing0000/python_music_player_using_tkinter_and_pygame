# import the files needed
import pygame
from music_controls import MusicControls
from tkinter import *

# create a class StopSong that inherits from the class MusicControls
class StopSong(MusicControls):
    
    def set_status(self):
        self.status.set("-Stopped")