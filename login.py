from tkinter import *
from tkinter import messagebox
import sqlite3
import register   # import register.py
import LMS        # import your main LMS.py


class Login_window:
    def __init__(self, window):
        self.window = window
        self.window.title("Login Window")
        self.window.geometry("1350x700+0+0")

        #===========Frame========
        login_frame = Frame(self.window, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"),
                      bg="white", fg="#08A3D2").place(x=250, y=50)

        Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"),
              bg="white", fg="gray").place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 18), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"),
              bg="white", fg="gray").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("times new roman", 18), bg="lightgray", show="*")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        Button(login_frame, cursor="hand2", command=self.register_window,
               text="Register new Account?", font=("times new roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=320)

        Button(login_frame, text="Login", command=self.login,
               font=("times new roman", 20), fg="white", bg="#B00857", cursor="hand2").place(x=250, y=380, width=180, height=40)

    def register_window(self):
        self.window.destroy()  # close login window
        root = Tk()
        register.Register(root)  # call Register class from register.py
        root.mainloop()

    def login(self):
        if self.txt_email.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.window)
        else:
            try:
                con = sqlite3.connect("LMS Project.db")
                cur = con.cursor()
                cur.execute('SELECT * FROM users WHERE email=? AND password=?',
                            (self.txt_email.get(), self.txt_pass_.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.window)
                else:
                    messagebox.showinfo("Success", f"Welcome : {self.txt_email.get()}", parent=self.window)
                    self.window.destroy()
                    root = Tk()
                    LMS.LMS(root)   # open your LMS main program
                    root.mainloop()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.window)


if __name__ == "__main__":
    root = Tk()
    Login_window(root)
    root.mainloop()
