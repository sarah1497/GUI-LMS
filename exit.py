from tkinter import *
from PIL import Image, ImageTk

class Exit: 
    def __init__(self, window):
        self.window = window
        self.window.title("Exit")
        self.window.geometry("400x200+500+250")
        self.window.configure(bg="#f0f0f0")
        self.window.focus_force()

        # Centered message
        Label(self.window, text="Click below to Exit Program", 
              font=("Arial", 16, "bold"), bg="#f0f0f0", fg="black").pack(pady=40)

        # Exit button
        Button(self.window, text="Exit", command=self.exit_app, 
               font=("Arial", 14, "bold"), bg="red", fg="white", width=12, cursor="hand2").pack(pady=20)

    def exit_app(self):
        self.window.quit()   # exits all tkinter windows


if __name__=="__main__":
    window = Tk()
    app = Exit(window)
    window.mainloop()
