# import the libraries needed
from tkinter import *
from tkinter import filedialog
import pygame
import os
from play_song import PlaySong
from stop_song import StopSong
from pause_song import PauseSong
from unpause_song import UnpauseSong

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
        self.folder_path = filedialog.askdirectory(title="Select a folder")
        if self.folder_path:
            os.chdir(self.folder_path)

        # Creating the Track Frames for Song label & status label
        track_frame = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="Navyblue",fg="white",bd=5,relief=GROOVE)
        track_frame.place(x=0,y=0,width=600,height=100)
        # Inserting Song Track Label
        song_track = Label(track_frame,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="Orange",fg="gold").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Status Label
        track_status = Label(track_frame,textvariable=self.status,font=("times new roman",24,"bold"),bg="orange",fg="gold").grid(row=0,column=1,padx=10,pady=5)

        # Creating Button Frame
        buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=100,width=600,height=100)
        # Inserting Play Button
        play_button = Button(buttonframe,text="PLAYSONG",command=self.play_song,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Pause Button
        play_button = Button(buttonframe,text="PAUSE",command=self.pause_song,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=1,padx=10,pady=5)
        # Inserting Unpause Button
        play_button = Button(buttonframe,text="UNPAUSE",command=self.unpause_song,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=2,padx=10,pady=5)
        # Inserting Stop Button
        play_button = Button(buttonframe,text="STOPSONG",command=self.stop_song,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=3,padx=10,pady=5)

        # Creating Playlist Frame
        songs_frame = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        songs_frame.place(x=600,y=0,width=400,height=200)
        # Inserting scrollbar
        scroll_y = Scrollbar(songs_frame,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songs_frame,yscrollcommand=scroll_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Fetching Songs
        song_tracks = os.listdir()
        # Inserting Songs into Playlist
        for track in song_tracks:
            self.playlist.insert(END,track)

    def play_song(self):
        play_song = PlaySong(self)
        play_song._MusicControls__set_status()
        play_song.play_song()
        
    def stop_song(self):
        stop_song = StopSong(self)
        stop_song._MusicControls__set_status()
        stop_song.stop_song()
    
    def pause_song(self):
        pause_song = PauseSong(self)
        pause_song._MusicControls__set_status()
        pause_song.pause_song()

    def unpause_song(self):
        unpause_song = UnpauseSong(self)
        unpause_song._MusicControls__set_status()
        unpause_song.unpause_song()