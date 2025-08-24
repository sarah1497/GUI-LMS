import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime


class StudentInfo:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1100x700+100+30")
        self.root.config(bg="white")

        # ---------------- Variables ---------------- #
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_state = StringVar()
        self.var_address = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_city = StringVar()
        self.var_postal = StringVar()
        self.var_admission = StringVar()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.create_db()

        # ---------------- Title ---------------- #
        title = Label(self.root, text="Student Management System",
                      font=("goudy old style", 20, "bold"), bg="#262626", fg="white")
        title.pack(side=TOP, fill=X)

        # ----------------  Frame ---------------- #
        frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        frame.place(x=10, y=50, width=450, height=630)

        # Labels & Entries
        Label(frame, text="Roll No", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=20)
        Entry(frame, textvariable=self.var_roll, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=20, width=200)

        Label(frame, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=60)
        Entry(frame, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=60, width=200)

        Label(frame, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=100)
        Entry(frame, textvariable=self.var_email, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=100, width=200)

        Label(frame, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=140)
        cmb_gender = ttk.Combobox(frame, textvariable=self.var_gender, values=("Male", "Female", "Other"), state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_gender.place(x=150, y=140, width=200)

        Label(frame, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=180)
        Entry(frame, textvariable=self.var_state, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=180, width=200)

        Label(frame, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=220)
        Entry(frame, textvariable=self.var_city, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=220, width=200)

        Label(frame, text="Postal Code", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=260)
        Entry(frame, textvariable=self.var_postal, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=260, width=200)

        Label(frame, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=300)
        Entry(frame, textvariable=self.var_address, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=300, width=200)

        Label(frame, text="D.O.B (dd/mm/yyyy)", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=340)
        Entry(frame, textvariable=self.var_dob, font=("goudy old style", 15), bg="lightyellow").place(x=220, y=340, width=130)

        Label(frame, text="Contact No", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=380)
        Entry(frame, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=380, width=200)

        Label(frame, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=420)
        Entry(frame, textvariable=self.var_course, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=420, width=200)

        Label(frame, text="Admission Date", font=("goudy old style", 15, "bold"), bg="white").place(x=30, y=460)
        Entry(frame, textvariable=self.var_admission, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=460, width=150)

        # Buttons
        Button(frame, text="Save", command=self.add, font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white").place(x=30, y=520, width=80)
        Button(frame, text="Update", command=self.update, font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white").place(x=120, y=520, width=80)
        Button(frame, text="Delete", command=self.delete, font=("goudy old style", 15, "bold"), bg="#f44336", fg="white").place(x=210, y=520, width=80)
        Button(frame, text="Clear", command=self.clear, font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white").place(x=300, y=520, width=80)

        # ---------------- Right Frame (Treeview) ---------------- #
        frame2 = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        frame2.place(x=470, y=50, width=620, height=630)

        # Search Panel
        lbl_search = Label(frame2, text="Search By:", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=10)
        cmb_search = ttk.Combobox(frame2, textvariable=self.var_searchby, values=("roll", "name", "contact"), state="readonly", justify=CENTER, font=("goudy old style", 13))
        cmb_search.place(x=120, y=10, width=150)
        Entry(frame2, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=280, y=10, width=150)
        Button(frame2, text="Search", command=self.search, font=("goudy old style", 13), bg="#03a9f4", fg="white").place(x=440, y=10, width=100)

        # Table Frame
        table_frame = Frame(frame2, bd=2, relief=RIDGE)
        table_frame.place(x=10, y=60, width=590, height=550)

        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)

        self.course_table = ttk.Treeview(table_frame, columns=("roll", "name", "email", "gender", "state", "city", "postal", "address", "dob", "contact", "course", "admission"),
                                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.course_table.yview)
        scroll_x.config(command=self.course_table.xview)

        self.course_table.heading("roll", text="Roll No")
        self.course_table.heading("name", text="Name")
        self.course_table.heading("email", text="Email")
        self.course_table.heading("gender", text="Gender")
        self.course_table.heading("state", text="State")
        self.course_table.heading("city", text="City")
        self.course_table.heading("postal", text="Postal Code")
        self.course_table.heading("address", text="Address")
        self.course_table.heading("dob", text="D.O.B")
        self.course_table.heading("contact", text="Contact No")
        self.course_table.heading("course", text="Course")
        self.course_table.heading("admission", text="Admission Date")

        self.course_table["show"] = "headings"

        for col in ("roll", "name", "email", "gender", "state", "city", "postal", "address", "dob", "contact", "course", "admission"):
            self.course_table.column(col, width=100)

        self.course_table.pack(fill=BOTH, expand=1)
        self.course_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # ---------------- Database ---------------- #
    def create_db(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student(
                roll TEXT PRIMARY KEY,
                name TEXT,
                email TEXT,
                gender TEXT,
                state TEXT,
                city TEXT,
                postal TEXT,
                address TEXT,
                dob TEXT,
                contact TEXT,
                course TEXT,
                admission TEXT
            )
        """)
        con.commit()
        con.close()

    # ---------------- Functions ---------------- #

    def show(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        self.course_table.delete(*self.course_table.get_children())
        for row in rows:
            self.course_table.insert("", END, values=row)
        con.close()

    def get_data(self, ev):
        f = self.course_table.focus()
        content = self.course_table.item(f)
        row = content["values"]
        if row:
            self.var_roll.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_state.set(row[4])
            self.var_city.set(row[5])
            self.var_postal.set(row[6])
            self.var_address.set(row[7])
            self.var_dob.set(row[8])
            self.var_contact.set(row[9])
            self.var_course.set(row[10])
            self.var_admission.set(row[11])

    def add(self):
        # Check all fields
        fields = {
            "Roll No": self.var_roll.get(),
            "Name": self.var_name.get(),
            "Email": self.var_email.get(),
            "Gender": self.var_gender.get(),
            "State": self.var_state.get(),
            "City": self.var_city.get(),
            "Postal Code": self.var_postal.get(),
            "Address": self.var_address.get(),
            "D.O.B": self.var_dob.get(),
            "Contact": self.var_contact.get(),
            "Course": self.var_course.get(),
            "Admission Date": self.var_admission.get()
        }
        for key, value in fields.items():
            if value == "" or value == "Select":
                messagebox.showerror("Error", f"{key} is required", parent=self.root)
                return

        # Validate DOB
        try:
            datetime.strptime(self.var_dob.get(), "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "D.O.B must be in format dd/mm/yyyy", parent=self.root)
            return

        # Insert into DB
        try:
            con = sqlite3.connect("student.db")
            cur = con.cursor()
            cur.execute("INSERT INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (
                self.var_roll.get(),
                self.var_name.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_state.get(),
                self.var_city.get(),
                self.var_postal.get(),
                self.var_address.get(),
                self.var_dob.get(),
                self.var_contact.get(),
                self.var_course.get(),
                self.var_admission.get()
            ))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Record Added Successfully", parent=self.root)
            self.show()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Roll No already exists", parent=self.root)

    def update(self):
        if self.var_roll.get() == "":
            messagebox.showerror("Error", "Select a record to update", parent=self.root)
            return

        # Roll No cannot be updated
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("SELECT roll FROM student WHERE roll=?", (self.var_roll.get(),))
        row = cur.fetchone()
        con.close()
        if not row:
            messagebox.showerror("Error", "Roll No cannot be updated", parent=self.root)
            return

        # Check all fields except Roll No
        fields = {
            "Name": self.var_name.get(),
            "Email": self.var_email.get(),
            "Gender": self.var_gender.get(),
            "State": self.var_state.get(),
            "City": self.var_city.get(),
            "Postal Code": self.var_postal.get(),
            "Address": self.var_address.get(),
            "D.O.B": self.var_dob.get(),
            "Contact": self.var_contact.get(),
            "Course": self.var_course.get(),
            "Admission Date": self.var_admission.get()
        }
        for key, value in fields.items():
            if value == "" or value == "Select":
                messagebox.showerror("Error", f"{key} is required", parent=self.root)
                return

        # Validate DOB
        try:
            datetime.strptime(self.var_dob.get(), "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "D.O.B must be in format dd/mm/yyyy", parent=self.root)
            return

        # Update DB
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("""UPDATE student SET
            name=?, email=?, gender=?, state=?, city=?, postal=?, address=?, dob=?, contact=?, course=?, admission=?
            WHERE roll=?""", (
            self.var_name.get(),
            self.var_email.get(),
            self.var_gender.get(),
            self.var_state.get(),
            self.var_city.get(),
            self.var_postal.get(),
            self.var_address.get(),
            self.var_dob.get(),
            self.var_contact.get(),
            self.var_course.get(),
            self.var_admission.get(),
            self.var_roll.get()
        ))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Record Updated Successfully", parent=self.root)
        self.show()



    def delete(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("DELETE FROM student WHERE roll=?", (self.var_roll.get(),))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Record Deleted Successfully", parent=self.root)
        self.show()

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_postal.set("")
        self.var_address.set("")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_course.set("")
        self.var_admission.set("")

    def search(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        if self.var_searchby.get() == "" or self.var_searchtxt.get() == "":
            messagebox.showerror("Error", "Search fields are required", parent=self.root)
            return
        cur.execute("SELECT * FROM student WHERE " + self.var_searchby.get() + " LIKE ?", ('%' + self.var_searchtxt.get() + '%',))
        rows = cur.fetchall()
        self.course_table.delete(*self.course_table.get_children())
        for row in rows:
            self.course_table.insert("", END, values=row)
        con.close()


if __name__ == "__main__":
    root = Tk()
    obj = StudentInfo(root)
    root.mainloop()
