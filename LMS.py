from tkinter import *
from PIL import Image, ImageTk

class LMS:
    def __init__(self, window):
        self.window = window
        self.window.title("Learning Management System")
        self.window.geometry("1200x600+70+70")
        self.window.configure(bg="#f0f0f0")

        #####ICONS####
        self.logo = Image.open("images/logo.png")
        # Main Title
        title = Label(self.window, text="Learning Management System",
                                    font=("Arial", 24, "bold"),
                                    bg="#004080", fg="white")



if __name__=="__main__":
    window = Tk()
    app = LMS(window)  # Create an instance of the LMS class
    window.mainloop()  # Start the main loop for the LMS application



