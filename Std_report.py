import sqlite3
from tkinter import *
from tkinter import messagebox

class Student_Report: 
    def __init__(self, window):
        self.window = window
        self.window.title("Student Report")
        self.window.geometry("1200x480+80+170")
        self.window.resizable(False, False)
        self.window.configure(bg="#ffffff")
        self.window.focus_force()

        #===Variables================
        self.var_search_roll = StringVar()
        self.result_data = {}  # store result data for display

        #===Title=======================
        Label(self.window, text="Student Result Management", font=("Arial", 20, "bold"),
              bg="#FAD503", fg="Black").place(x=10, y=15, width=1230, height=50)

        #===search frame=======================
        Label(self.window, text="Search Student By Roll No.", font=("Arial", 15, "bold"),
              bg="#FFFFFF").place(x=250, y=100)
        Entry(self.window, font=("Arial", 15), bg="Light yellow", textvariable=self.var_search_roll).place(x=550, y=100, width=150,height=35)

        #===Button=======================
        Button(self.window, text="Search", font=("goudy old style", 15 , "bold"),
               bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=710, y=100, width=100, height=35)
        Button(self.window, text="Clear", font=("goudy old style", 15 , "bold"),
               bg="grey", fg="white", cursor="hand2", command=self.clear).place(x=820, y=100, width=100, height=35)
        Button(self.window, text="Delete", font=("goudy old style", 15, "bold"),
               bg="red", fg="white", cursor="hand2", command=self.delete).place(x=500, y=350, width=120, height=35)

        #===Result Label=======================
        headers = ["Roll No", "Name", "Course", "Marks Obtained", "Full Marks", "Percentage"]
        x_positions = [150, 300, 450, 600, 750, 900]
        self.labels = {}  # dictionary to store Label widgets
        for i, head in enumerate(headers):
            Label(self.window, text=head, font=("Arial", 15), relief=GROOVE).place(x=x_positions[i], y=230,width=150,height=50)
            self.labels[head] = Label(self.window, font=("Arial", 15), relief=GROOVE)
            self.labels[head].place(x=x_positions[i], y=280, width=150, height=50)

    #===Search Function==================
    def search(self):
        roll = self.var_search_roll.get()
        if roll == "":
            messagebox.showerror("Error", "Please enter Roll No", parent=self.window)
            return
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM result WHERE roll=?", (roll,))
        row = cur.fetchone()
        con.close()
        if row:
            self.labels["Roll No"].config(text=row[0])
            self.labels["Name"].config(text=row[1])
            self.labels["Course"].config(text=row[2])
            self.labels["Marks Obtained"].config(text=row[3])
            self.labels["Full Marks"].config(text=row[4])
            percentage = (row[3]/row[4]*100) if row[4] != 0 else 0
            self.labels["Percentage"].config(text=f"{percentage:.2f}%")
        else:
            messagebox.showerror("Error", "No record found", parent=self.window)
            self.clear()

    #===Clear Function===================
    def clear(self):
        for key in self.labels:
            self.labels[key].config(text="")
        self.var_search_roll.set("")

    #===Delete Function==================
    def delete(self):
        roll = self.var_search_roll.get()
        if roll == "":
            messagebox.showerror("Error", "Enter Roll No to delete", parent=self.window)
            return
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("DELETE FROM result WHERE roll=?", (roll,))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Record Deleted Successfully", parent=self.window)
        self.clear()


if __name__=="__main__":
    window = Tk()
    app = Student_Report(window)
    window.mainloop()
