from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import login   # make sure login.py exists in the same folder

class Register:
    def __init__(self, window):
        self.window = window
        self.window.title("Registration Window")
        self.window.geometry("1350x700+0+0")

        #===Register Frame====
        frame1 = Frame(self.window, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"),
                      bg="white", fg="green").place(x=50, y=30)

        #=======================Row1
        Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        #=======================Row2
        Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        #=======================Row3
        Label(frame1, text="Security Question.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_quest['values'] = ("Select", "Your first pet name", "Your birth place", "Your best friend name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        #======================Row4
        Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_password.place(x=50, y=340, width=250)

        Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_cpassword.place(x=370, y=340, width=250)

        #===========Terms=========
        self.var_chk = IntVar()
        Checkbutton(frame1, text="I Agree The Terms & Conditions.", variable=self.var_chk,
                    onvalue=1, offvalue=0, bg="white", font=("times new roman", 12)).place(x=50, y=380) 

        # Register Button
        Button(frame1, text="Register", font=("times new roman", 20, "bold"), bg="#08A3D2", fg="white",
               cursor="hand2", command=self.register_data).place(x=50, y=430, width=180, height=40)

        # Already have account? -> Login
        Button(frame1, text="Already Registered? Login", font=("times new roman", 15), bg="white", fg="#B00857",
               bd=0, cursor="hand2", command=self.open_login).place(x=250, y=440)

    def open_login(self):
        """ Open login window """
        self.window.destroy()
        root = Tk()
        obj = login.Login_window(root)
        root.mainloop()

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)
        self.var_chk.set(0)

    def register_data(self):
        if (self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_contact.get() == "" or 
            self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or
            self.txt_password.get() == "" or self.txt_cpassword.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.window)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.window)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree Our Terms & Conditions", parent=self.window)
        else:
            try:
                con = sqlite3.connect("LMS Project.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, Please try another email", parent=self.window)
                else:
                    cur.execute("INSERT INTO users(f_name, l_name, contact, email, question, answer, password) VALUES(?,?,?,?,?,?,?)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.cmb_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Registered Successfully", parent=self.window)
                    con.close()
                    self.open_login()   # open login window automatically
            except Exception as es:
                messagebox.showerror("Error", f"Error Due To: {str(es)}", parent=self.window)


if __name__ == "__main__":
    window = Tk()
    obj = Register(window)
    window.mainloop()
