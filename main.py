# import the needed files
from music_player import MusicPlayer
from tkinter import *

if __name__ == "__main__":
    root = Tk() # In order to create an empty window
# Passing Root to MusicPlayer Class
MusicPlayer(root)

root.mainloop()