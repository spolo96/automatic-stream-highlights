# Python TKinter - Automatic Streaming Highlights Desktop Application
# By Samuel David "WolflyPolo" Polo Peña
# License code: Creative Commons 0 - Public Domain

# importing only those functions
# which are needed
import tkinter as tk
from tkinter import ttk
from time import strftime
import os
from pymediainfo import MediaInfo
from automatic_highlights_module import get_automatic_highlights

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile
import threading

_video = None

# Creating tkinter window
root = tk.Tk()
root.geometry('800x560')
root.title('Automatic Streaming Highlights - WolflyPolo')

# Creating Menubar
menubar = tk.Menu(root)

# Adding File Menu and commands
file = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Open...', command = lambda:open_file())
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Help Menu
help_ = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='How to Use', command = None)
help_.add_command(label ='Known Issues', command = None)
help_.add_separator()
help_.add_command(label ='About this app', command = None)

# Loading a Video Functions -----------------------------------------------------------------------------------------
# This function will be used to open a single video in .mp4
def open_file():
    video = askopenfile(mode ='r', filetypes =[('Video Files', '*.mp4')])
    if video is not None:
        video = video.name
        print(video)
        global _video
        _video = video
        see_properties(video)

# See Properties of a Video that has been loaded successfully.
def see_properties(file):
    size = os.path.getsize(file) // 1000000
    duration = MediaInfo.parse(file)
    ms = int(duration.tracks[0].duration / 3600) *4
    filedata = f"File size: {size:n} MB\nDuration: {ms} seconds"

    _duration = f"{ms} seconds"
    _size = f"{size:n} MB"
    
    videoDuration.config(text = "Video Duration: "+str(_duration))
    videoSize.config(text = "Video Size: "+str(_size))

    print(filedata)

# --------------------------------------------------------------------------------------------------------------------
def start_automatic_highlights():
    threading.Thread(target=automatic_highlights).start()

def automatic_highlights():
    if _video is None:
        btn2.config(text = "Video Not Selected!")
    else:
        print(_video)
        btn2.config(text = "Creating automatic highlights...")
        pb.start()
        get_automatic_highlights(_video)
        pb.stop()
        btn2.config(text = "Highlight Created! Open another video to create another highlight!")

# Video Details Labels -----------------------------------------------------------------------------------------------

videoDuration = tk.Label(root, text = "Video Duration: No video selected.")
videoDuration.place(x = 40, y = 100)  

videoSize = tk.Label(root, text = "Video Size: No video selected.")
videoSize.place(x = 40, y = 140)

# --------------------------------------------------------------------------------------------------------------------

la = tk.Label(root, text = "Select a video file to automatically create highlights!")
la.pack()

btn = tk.Button(root, text ='Open', command = lambda:open_file())
btn.pack(side = tk.TOP, pady = 10)

btn2 = tk.Button(root, text ='Get my automatic highlights!', command = start_automatic_highlights) 

btn2.pack(side = tk.TOP, pady = 40)

# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=280
)

pb.place(x=250, y=250, width=350)

# Display Menu
root.config(menu = menubar)
root.mainloop()
