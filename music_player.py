# import the libraries needed
from tkinter import *
import pygame
import os

# Create MusicPlayer Class
class MusicPlayer():
    
    def __init__(self, root):
        self.root = root
        # Title of the window
        self.root.title("MusicPlayer")
        # Window Geometry
        self.root.geometry("1000x200+200+200")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()