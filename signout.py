from tkinter import *
from PIL import Image, ImageTk

class sign_out: 
    def __init__(self, window):
        self.window = window
        self.window.title("Sign Out")
        self.window.geometry("1350x700+0+0")
        self.window.configure(bg="#f0f0f0")
        self.window.focus_force()





if __name__=="__main__":
    window = Tk()
    app = sign_out(window)  # Create an instance of the LMS class
    window.mainloop()  # Start the main loop for the LMS application
