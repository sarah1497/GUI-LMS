from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class C_class: 
    def __init__(self, window):
        self.window = window
        self.window.title("Courses Information")
        self.window.geometry("1250x500+0+0")
        self.window.minsize(1250, 500)
        self.window.configure(bg="#ffffff")
        self.window.focus_force()

        #===Variables===================
        self.var_course_name = StringVar()
        self.var_teacher_name = StringVar()
        self.var_course_code = StringVar()
        self.var_shift = StringVar()
        self.var_search = StringVar()

        # Ensure DB + Table exists
        self.create_db()

        #===Title=======================
        Label(self.window, text="Manage Course Details", font=("Arial", 20, "bold"),
              bg="#004080", fg="white").place(x=10, y=15, width=1230, height=35)

        #===Labels======================
        Label(self.window, text="Course Name", font=("Arial", 15, "bold"), bg="#FFFFFF").place(x=10, y=80)
        Label(self.window, text="Teacher Name", font=("Arial", 15, "bold"), bg="#FFFFFF").place(x=10, y=120)
        Label(self.window, text="Course Code", font=("Arial", 15, "bold"), bg="#FFFFFF").place(x=10, y=160)
        Label(self.window, text="Shift", font=("Arial", 15, "bold"), bg="#FFFFFF").place(x=10, y=200)

        #===Entries=====================
        Entry(self.window, textvariable=self.var_course_name, font=("Arial", 15, "bold"),
              bg="light yellow").place(x=170, y=80, width=450)
        Entry(self.window, textvariable=self.var_teacher_name, font=("Arial", 15, "bold"),
              bg="light yellow").place(x=170, y=120, width=450)
        Entry(self.window, textvariable=self.var_course_code, font=("Arial", 15, "bold"),
              bg="light yellow").place(x=170, y=160, width=450)
        Entry(self.window, textvariable=self.var_shift, font=("Arial", 15, "bold"),
              bg="light yellow").place(x=170, y=200, width=450)  # Normal Entry for Shift

        #===Search Panel================
 
        Label(self.window, text="Search", font=("Arial", 15, "bold"), bg="#FFFFFF").place(x=720, y=60)
        Entry(self.window, textvariable=self.var_search, font=("Arial", 15, "bold"), bg="light yellow").place(x=800, y=60, width=280)
        Button(self.window, text="Search", font=("Arial", 15, "bold"),
            bg="#2196f3", fg="white", cursor="hand2", command=self.search).place(x=1100, y=60, width=140, height=30)

        #===Table Frame=================
        self.course_Frame = Frame(self.window, bd=2, relief=RIDGE)
        self.course_Frame.place(x=720, y=100, width=520, height=350)

        self.course_table = ttk.Treeview(self.course_Frame,
                                         columns=("Course Name", "Teacher Name", "Course Code", "Shift"),
                                         show='headings')
        self.course_table.pack(fill=BOTH, expand=1)

        #===Headings====================
        self.course_table.heading("Course Name", text="Course Name")
        self.course_table.heading("Teacher Name", text="Teacher Name")
        self.course_table.heading("Course Code", text="Course Code")
        self.course_table.heading("Shift", text="Shift")

        self.course_table.column("Course Name", width=120)
        self.course_table.column("Teacher Name", width=120)
        self.course_table.column("Course Code", width=120)
        self.course_table.column("Shift", width=80)
        self.course_table.bind("<ButtonRelease-1>", self.get_data)
        
        #===Buttons=====================
        Button(self.window, text="Save", font=("Arial", 15, "bold"), 
               bg="#2196f3", fg="white", cursor="hand2", command=self.add).place(x=170, y=400, width=100, height=40)
        Button(self.window, text="Update", font=("Arial", 15, "bold"), 
               bg="#4caf50", fg="white", cursor="hand2", command=self.update).place(x=280, y=400, width=100, height=40)
        Button(self.window, text="Delete", font=("Arial", 15, "bold"), 
               bg="#f44336", fg="white", cursor="hand2", command=self.delete).place(x=390, y=400, width=100, height=40)
        Button(self.window, text="Clear", font=("Arial", 15, "bold"), 
               bg="#607d8b", fg="white", cursor="hand2", command=self.clear).place(x=500, y=400, width=100, height=40)

        # Load data on startup
        self.show_courses()

    #===Get Data from Table============
    def get_data(self, event):
        selected_row = self.course_table.focus()
        content = self.course_table.item(selected_row)
        row = content['values']
        if row:
            self.var_course_name.set(row[0])
            self.var_teacher_name.set(row[1])
            self.var_course_code.set(row[2])
            self.var_shift.set(row[3])

    #===Database Setup=================
    def create_db(self):
        con = sqlite3.connect("LMS Project.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS course (
                course_name TEXT,
                teacher_name TEXT,
                course_code TEXT UNIQUE,
                shift TEXT
            )
        """)
        con.commit()
        con.close()

    #===Add New Course=================
    def add(self):
        con = sqlite3.connect("LMS Project.db")
        cur = con.cursor()
        try:
            if self.var_course_name.get() == "" or self.var_course_code.get() == "":
                messagebox.showerror("Error", "Course Name and Code are required", parent=self.window)
            else:
                cur.execute("SELECT * FROM course WHERE course_code=?", (self.var_course_code.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", f"Course Code {self.var_course_code.get()} already exists", parent=self.window)
                else: 
                    cur.execute("INSERT INTO course(course_name, teacher_name, course_code, shift) VALUES (?,?,?,?)",
                                (self.var_course_name.get(),
                                 self.var_teacher_name.get(),
                                 self.var_course_code.get(),
                                 self.var_shift.get())) 
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.window)
                    self.show_courses()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.window)
        finally:
            con.close()

    #===Update Course=================
    def update(self):
        con = sqlite3.connect("LMS Project.db")
        cur = con.cursor()
        try:
            if self.var_course_code.get() == "":
                messagebox.showerror("Error", "Select a course to update", parent=self.window)
            else:
                cur.execute("SELECT * FROM course WHERE course_code=?", (self.var_course_code.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Course not found", parent=self.window)
                else:
                    cur.execute("""
                        UPDATE course SET course_name=?, teacher_name=?, shift=?
                        WHERE course_code=?
                    """, (
                        self.var_course_name.get(),
                        self.var_teacher_name.get(),
                        self.var_shift.get(),
                        self.var_course_code.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Updated Successfully", parent=self.window)
                    self.show_courses()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.window)
        finally:
            con.close()

    #===Delete Course=================
    def delete(self):
        con = sqlite3.connect("LMS Project.db")
        cur = con.cursor()
        try:
            if self.var_course_code.get() == "":
                messagebox.showerror("Error", "Select a course to delete", parent=self.window)
            else:
                confirm = messagebox.askyesno("Confirm", "Do you really want to delete this course?", parent=self.window)
                if confirm:
                    cur.execute("DELETE FROM course WHERE course_code=?", (self.var_course_code.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Course Deleted Successfully", parent=self.window)
                    self.show_courses()
                    self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.window)
        finally:
            con.close()

    #===Clear Fields==================
    def clear(self):
        self.var_course_name.set("")
        self.var_teacher_name.set("")
        self.var_course_code.set("")
        self.var_shift.set("")

    #===Show Courses===================
    def show_courses(self):
        con = sqlite3.connect("LMS Project.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM course")
        rows = cur.fetchall()
        self.course_table.delete(*self.course_table.get_children())
        for row in rows:
            self.course_table.insert('', END, values=row)
        con.close()
    def search(self):
        con = sqlite3.connect("LMS Project.db")
        cur = con.cursor()
        try:
            search_value = self.var_search.get().strip()
            if search_value == "":
                # Show all courses if search box is empty
                self.show_courses()
            else:
                cur.execute("SELECT * FROM course WHERE course_name LIKE ?", ('%' + search_value + '%',))
                rows = cur.fetchall()
                self.course_table.delete(*self.course_table.get_children())
                for row in rows:
                    self.course_table.insert('', END, values=row) 
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.window)
        finally:
            con.close()
            con = sqlite3.connect("LMS Project.db")
            cur = con.cursor()
            try:
                search_value = self.var_search.get().strip()
                if search_value == "":
                    messagebox.showerror("Error", "Enter a course name to search", parent=self.window)
                else:
                    cur.execute("SELECT * FROM course WHERE course_name LIKE ?", ('%' + search_value + '%',))
                    rows = cur.fetchall()
                    self.course_table.delete(*self.course_table.get_children())
                    for row in rows:
                        self.course_table.insert('', END, values=row) 
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.window)
            finally:
                con.close()

if __name__=="__main__":
    window = Tk()
    app = C_class(window)
    window.mainloop()
