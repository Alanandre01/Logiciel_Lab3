from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sys

#sys.path.append("C:\\Users\\alana\\Downloads\\Logiciel_Lab3\\x64\\Debug")

import Lab3_Cpp

#import PIL.Image, PIL.ImageTk
#import cv2

class videoGUI:

    def __init__(self, window, window_title):

        self.window = window
        self.window.title(window_title)

        top_frame = Frame(self.window)
        top_frame.pack(side=TOP, pady=5)

        bottom_frame = Frame(self.window)
        bottom_frame.pack(side=BOTTOM, pady=5)

        #Etats de la vidéo
        self.pause = False
        self.stop = True
        self.open = False

        self.canvas = Canvas(top_frame,width=1000, height=600, )
        self.canvas.pack()

        # Select Button
        self.btn_select=Button(bottom_frame, text="Select video file", width=15, command=self.open_file)
        self.btn_select.grid(row=0, column=0)

        # Play/Pause Button
        self.btn_play=Button(bottom_frame, text="Play/Pause", width=15, command=Lab3_Cpp.inputChar("p"))
        self.btn_play.grid(row=0, column=1)

        # Stop Button
        self.btn_pause=Button(bottom_frame, text="Stop", width=15, command=Lab3_Cpp.inputChar("q"))
        self.btn_pause.grid(row=0, column=3)

        # Back Button
        self.btn_back=Button(bottom_frame, text="Back to start", width=15, command=Lab3_Cpp.inputChar("r"))
        self.btn_back.grid(row=0, column=4)

        # Quit Button
        self.btn_quit=Button(bottom_frame, text="Quit", width=15, command=self.quit)
        self.btn_quit.grid(row=0, column=4)

        #self.delay = 30  # ms

        self.window.mainloop()


    def open_file(self):

        self.pause = False

        self.filename = filedialog.askopenfilename(title="Select file", filetypes=(("AVI files", "*.avi"), ("MP4 files", "*.mp4"),
                                                                                         ("WMV files", "*.wmv")))
        Lab3_Cpp.initModule(self.filename)

        #print(self.filename)

        ## Open the video file
        #self.cap = cv2.VideoCapture(self.filename)

        #self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        #self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
       
        #self.canvas.config(width = self.width, height = self.height)

        #self.open = True
        #self.stop = False
        #self.run_video()


    #def get_frame(self):   # get only one frame

    #    try:

    #        if self.cap.isOpened():
    #            ret, frame = self.cap.read()
    #            return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    #    except:
    #        messagebox.showerror(title='Video file not found', message='Please select a video file.')
    
    ##Play button
    #def play_video(self):
        
    #    self.stop = False

    #    if self.pause == True:
    #        self.pause = False
    #        self.run_video()
    
    ##Pause button
    #def pause_video(self):
    #    self.pause = True

    #def run_video(self):

    #    # Get a frame from the video source, and go to the next frame automatically
    #    if self.open == True:
    #        ret, frame = self.get_frame() 
         
    #        self.pos = self.cap.get(cv2.CAP_PROP_POS_FRAMES)        #Frame position
    #        self.length = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)    #Total frame

    #        if ret:
    #            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    #            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
            
    #        # Loop at the end of the video
    #        if self.pos == self.length:
    #            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0.0)

    #        if self.pause:
    #            self.window.after_cancel(self.after_id)
    #        else:
    #            self.after_id = self.window.after(self.delay, self.run_video)
   
    #Pause button
    def quit(self):

        self.stop = True
        self.open = False

        #self.cap.release()
        self.canvas.delete("all")
        #cv2.destroyAllWindows()
        
    #Back button
    #def back_video(self):

    #    self.cap.set(cv2.CAP_PROP_POS_FRAMES,0.0) #set frame position
    
    # Release the video source when the object is destroyed
    #def __del__(self):

    #    if self.cap.isOpened():
    #        self.cap.release()

##### End Class #####


# Create a window and pass it to videoGUI Class
videoGUI(Tk(), "Video Player")