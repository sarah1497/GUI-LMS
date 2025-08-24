from tkinter import *
from PIL import Image, ImageTk
import time
from tkinter import messagebox
import os

class LMS: 
    def __init__(self, window):
        self.window = window
        self.window.title("Learning Management System")
        self.window.geometry("1350x700+0+0")
        self.window.configure(bg="#f0f0f0")

      
        # Main Title
        title = Label(self.window, text="Learning Management System",                                  
                                    font=("Arial", 24, "bold"),
                                    bg="#004080", fg="white").place(x=0, y=0, relwidth=1, height=50)
        # Clock Label (top-right)
        self.clock_label = Label(self.window, font=("Arial", 12, "bold"), bg="#004080", fg="white")
        self.clock_label.place(x=1150, y=10)  
        self.update_clock()  # start clock 
       #=Menu==================
        Menu_F = LabelFrame(self.window, text="Menu", bg="#FFFFFF", 
                            font=("Arial", 12)).place(x=10, y=70, width=1340, height=80)
       #=Buttons==================
        Button(Menu_F, text="Courses", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_course_window,font=("Arial", 12)).place(x=20, y=100, width=200, height=40)
        Button(Menu_F, text="Student Info", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_std_window,font=("Arial", 12)).place(x=240, y=100, width=200, height=40)
        Button(Menu_F, text="Result", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_Result_window,font=("Arial", 12)).place(x=460, y=100, width=200, height=40)
        Button(Menu_F, text="View Result", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_Student_Report_window,font=("Arial", 12)).place(x=680, y=100, width=200, height=40)
        Button(Menu_F, text="sign out", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_sign_out_window,font=("Arial", 12)).place(x=900, y=100, width=200, height=40)
        Button(Menu_F, text="Exit", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_exit_window,font=("Arial", 12)).place(x=1120, y=100, width=200, height=40)
        #=Content window==================
        self.bg_img = Image.open("Img/bg.png").resize((920, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.window, image=self.bg_img).place(x=230, y=220, width=920, height=350)

        #=Update Details==================
        self.lbl_Course = Label(self.window, text="Total Courses\n[ 0 ]", bg="#004080", fg="white", font=("Arial", 
                                20, "bold"), bd=5, relief=RIDGE).place(x=350, y=580, width=300, height=100)
        self.lbl_result = Label(self.window, text="Total Result\n[ 0 ]", bg="#004080", fg="white", font=("Arial", 
                                20, "bold"), bd=5, relief=RIDGE).place(x=700, y=580, width=300, height=100)
   
    #=Clock==================
    def update_clock(self):
        current_time = time.strftime("%Y-%m-%d  %H:%M:%S")
        self.clock_label.config(text=current_time)
        self.clock_label.after(1000, self.update_clock)
    
    #=Open Course Window==================
    def open_course_window(self): 
        from course import C_class
        self.new_window = Toplevel(self.window)
        self.app = C_class(self.new_window)
    #=Open Student Info Window==================
    def open_std_window(self):
        from Std_info import StudentInfo
        self.new_window = Toplevel(self.window)
        self.app = StudentInfo(self.new_window)

    #=Open Result Window==================
    def open_Result_window(self):
        from Result import Result
        self.new_window = Toplevel(self.window)
        self.app = Result(self.new_window)

    #=Open Student_report Window==================
    def open_Student_Report_window(self):  
        from Std_report import Student_Report
        self.new_window = Toplevel(self.window)
        self.app = Student_Report(self.new_window)

    #=Open sign Out Window==================
    def open_sign_out_window(self):  
        from signout import sign_out
        self.new_window = Toplevel(self.window)
        self.app = sign_out(self.new_window)
    
    #=Open Exit Window==================
    def open_exit_window(self):
        from exit import Exit
        self.new_window = Toplevel(self.window)
        self.app = Exit(self.new_window)
    def signout(self):
        op=messagebox.askyesno("confirm", "do you really want to signout?",parent=self.window)
        if op==True:
            self.window.destroy()
            os.system("python signin.py")
    def exit_(self):
        op=messagebox.askyesno("confirm", "do you really want to exit?",parent=self.window)
        if op==True:
            self.window.destroy()

if __name__=="__main__":
    window = Tk()
    app = LMS(window)  # Create an instance of the LMS class
    window.mainloop()  # Start the main loop for the LMS application



