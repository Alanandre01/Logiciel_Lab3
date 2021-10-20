from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import sys

sys.path.append("C:\\Users\\abrucher\\Downloads\\Logiciel_Lab3\\x64\\Debug")

import Lab3_Cpp


class videoGUI:
    def __init__(self, window, window_title):

        self.window = window
        self.window.title(window_title)

        top_frame = Frame(self.window)
        top_frame.pack(side=TOP, pady=5)

        bottom_frame = Frame(self.window)
        bottom_frame.pack(side=BOTTOM, pady=5)

        # Etats de la vidéo
        self.pause = False
        self.stop = True
        self.open = False

        self.canvas = Canvas(top_frame, width=600, height=0)
        self.canvas.pack()

        # Select File Button
        self.btn_select = Button(
            bottom_frame, text="Select video file", width=15, command=self.open_file
        )
        self.btn_select.grid(row=0, column=0)

        # Play/Pause Button
        self.btn_play = Button(
            bottom_frame,
            text="Play/Pause",
            width=15,
            command=lambda: Lab3_Cpp.inputChar("p"),
        )
        self.btn_play.grid(row=0, column=1)

        # Stop Button
        self.btn_pause = Button(
            bottom_frame, text="Stop", width=15, command=lambda: Lab3_Cpp.inputChar("s")
        )
        self.btn_pause.grid(row=0, column=3)

        # Back Button
        self.btn_back = Button(
            bottom_frame,
            text="Back to start",
            width=15,
            command=lambda: Lab3_Cpp.inputChar("r"),
        )
        self.btn_back.grid(row=0, column=4)

        # Quit Button
        self.btn_quit = Button(
            bottom_frame, text="Quit", width=15, command=lambda: Lab3_Cpp.inputChar("q")
        )
        self.btn_quit.grid(row=0, column=5)

        self.window.mainloop()

    def open_file(self):

        self.pause = False

        self.filename = filedialog.askopenfilename(
            title="Select file",
            filetypes=(
                ("AVI files", "*.avi"),
                ("MP4 files", "*.mp4"),
                ("WMV files", "*.wmv"),
            ),
        )
        Lab3_Cpp.initModule(self.filename)


# Create a window and pass it to videoGUI Class
videoGUI(Tk(), "Video Player")
