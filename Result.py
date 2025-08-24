from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class Result: 
    def __init__(self, window):
        self.window = window
        self.window.title("Result")
        self.window.geometry("1250x500+0+0")
        self.window.resizable(False, False)
        self.window.configure(bg="#f0f0f0")
        self.window.focus_force()

        #===Title=======================
        Label(self.window, text="Add Student Result", font=("Arial", 20, "bold"),
              bg="#FAD503", fg="Black").place(x=10, y=15, width=1230, height=50)

        #===Variable=============
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_fullmarks=StringVar()
        self.roll_list=[]

        # Fetch student roll numbers
        self.fetch_rolls()

        #===Widget=======================
        Label(self.window, text="Select Student", font=("Arial", 15, "bold")).place(x=50, y=80)
        Label(self.window, text="Name", font=("Arial", 15, "bold")).place(x=50, y=130)
        Label(self.window, text="Course", font=("Arial", 15, "bold")).place(x=50, y=180)
        Label(self.window, text="Marks Obtained", font=("Arial", 15, "bold")).place(x=50, y=230)
        Label(self.window, text="Full Marks", font=("Arial", 15, "bold")).place(x=50, y=280)

        self.cmb_student = ttk.Combobox(self.window, textvariable=self.var_roll, values=self.roll_list,
                                   state="readonly", justify=CENTER, font=("goudy old style", 15))
        self.cmb_student.place(x=250, y=80, width=200)
        self.cmb_student.set("Select")

        #===Entry=======================
        Entry(self.window, textvariable= self.var_name,font=("Arial", 15),bg="Light yellow", state="readonly").place(x=250, y=130, width=370, height=35)
        Entry(self.window, textvariable= self.var_course,font=("Arial", 15),bg="Light yellow", state="readonly").place(x=250, y=180, width=370, height=35)
        Entry(self.window, textvariable=self.var_marks,font=("Arial", 15),bg="Light yellow").place(x=250, y=230, width=370, height=35)
        Entry(self.window, textvariable=self.var_fullmarks,font=("Arial", 15),bg="Light yellow").place(x=250, y=280, width=370, height=35)
        
        #===Button=======================
        Button(self.window, text="Search", command=self.search, font=("goudy old style", 15, "bold"),
               bg="#03a9f4", fg="white",cursor="hand2").place(x=500, y=80, width=120, height=28)
        Button(self.window, text="Add", command=self.add, font=("goudy old style", 15, "bold"),
               bg="Light green", activebackground="light green",cursor="hand2").place(x=300, y=350, width=120, height=35)
        Button(self.window, text="Clear", command=self.clear, font=("goudy old style", 15, "bold"),
               bg="light grey", activebackground="light grey",cursor="hand2").place(x=440, y=350, width=120, height=35)
        
        #===Image=======================
        self.bg_img = Image.open("Img/result.png").resize((500, 300), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.window, image=self.bg_img).place(x=700, y=80, width=500, height=300)


    #===Function to fetch student roll numbers
    def fetch_rolls(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("SELECT roll FROM student")
        rows = cur.fetchall()
        con.close()
        self.roll_list = [str(r[0]) for r in rows]

    #===Search Student
    def search(self):
        if self.var_roll.get()=="Select":
            messagebox.showerror("Error", "Please select a student", parent=self.window)
            return
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("SELECT name, course FROM student WHERE roll=?", (self.var_roll.get(),))
        row = cur.fetchone()
        con.close()
        if row:
            self.var_name.set(row[0])
            self.var_course.set(row[1])
        else:
            messagebox.showerror("Error", "No record found", parent=self.window)

    #===Add Result
    #===Add Result
    def add(self):
        if self.var_roll.get()=="Select" or self.var_name.get()=="" or self.var_course.get()=="":
            messagebox.showerror("Error", "Please search and select student first", parent=self.window)
            return
        if self.var_marks.get()=="" or self.var_fullmarks.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.window)
            return
        try:
            marks = int(self.var_marks.get())
            full = int(self.var_fullmarks.get())
            if marks > full:
                messagebox.showerror("Error", "Marks cannot be greater than Full Marks", parent=self.window)
                return
        except:
            messagebox.showerror("Error", "Marks and Full Marks must be numbers", parent=self.window)
            return

        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS result(roll TEXT PRIMARY KEY, name TEXT, course TEXT, marks INTEGER, fullmarks INTEGER)")
        
        # check if result already exists for this roll
        cur.execute("SELECT * FROM result WHERE roll=?", (self.var_roll.get(),))
        row = cur.fetchone()
        if row:
            messagebox.showerror("Error", "Result for this student already exists and cannot be updated", parent=self.window)
            con.close()
            return

        # insert result
        cur.execute("INSERT INTO result VALUES (?,?,?,?,?)", (
            self.var_roll.get(),
            self.var_name.get(),
            self.var_course.get(),
            self.var_marks.get(),
            self.var_fullmarks.get()
        ))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Result Added Successfully", parent=self.window)
        self.clear()

    #===Clear fields
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_fullmarks.set("")


if __name__=="__main__":
    window = Tk()
    app = Result(window)
    window.mainloop()
