from tkinter import *
from tkinter import messagebox
import os

class sign_out: 
    def __init__(self, window):
        self.window = window
        self.window.title("Sign Out")
        self.window.geometry("400x200+500+250")
        self.window.configure(bg="#f0f0f0")
        self.window.focus_force()

        # Message
        Label(self.window, text="Do you want to Sign Out?", 
              font=("Arial", 16, "bold"), bg="#f0f0f0", fg="black").pack(pady=30)

        # Buttons
        btn_frame = Frame(self.window, bg="#f0f0f0")
        btn_frame.pack(pady=20)

        Button(btn_frame, text="Yes", command=self.sign_out_app, 
               font=("Arial", 14, "bold"), bg="green", fg="white", width=8, cursor="hand2").grid(row=0, column=0, padx=10)

        Button(btn_frame, text="No", command=self.window.destroy, 
               font=("Arial", 14, "bold"), bg="red", fg="white", width=8, cursor="hand2").grid(row=0, column=1, padx=10)

    def sign_out_app(self):
        self.window.destroy()
        os.system("python login.py")  # Opens Login page again


if __name__=="__main__":
    window = Tk()
    app = sign_out(window)
    window.mainloop()
