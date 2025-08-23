from tkinter import *
from PIL import Image, ImageTk
import time

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
        Course_Button = Button(Menu_F, text="Courses", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_course_window,font=("Arial", 12)).place(x=20, y=100, width=200, height=40)
        Std_info_Button = Button(Menu_F, text="Student Info", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_std_window,font=("Arial", 12)).place(x=240, y=100, width=200, height=40)
        Assignment_Button = Button(Menu_F, text="Assignments", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_assignment_window,font=("Arial", 12)).place(x=460, y=100, width=200, height=40)
        Result_Button = Button(Menu_F, text="Result", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_Result_window,font=("Arial", 12)).place(x=680, y=100, width=200, height=40)
        View_Result_Button = Button(Menu_F, text="View Result", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_View_Result_window,font=("Arial", 12)).place(x=900, y=100, width=200, height=40)
        Logout_Button = Button(Menu_F, text="Log out", bg="#004080", fg="white", cursor="hand2",
                               command= self.open_Log_out_window,font=("Arial", 12)).place(x=1120, y=100, width=200, height=40)
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
        from Std_info import std_info
        self.new_window = Toplevel(self.window)
        self.app = std_info(self.new_window)

    #=Open Assignment Window==================
    def open_assignment_window(self):
        from assignments import Assignment
        self.new_window = Toplevel(self.window)
        self.app = Assignment(self.new_window)

    #=Open Result Window==================
    def open_Result_window(self):
        from Result import Result
        self.new_window = Toplevel(self.window)
        self.app = Result(self.new_window)

    #=Open View_Result Window==================
    def open_View_Result_window(self):  
        from View_Result import View_Result
        self.new_window = Toplevel(self.window)
        self.app = View_Result(self.new_window)

    #=Open Log Out Window==================
    def open_Log_out_window(self):  
        from signout import sign_out
        self.new_window = Toplevel(self.window)
        self.app = sign_out(self.new_window)


if __name__=="__main__":
    window = Tk()
    app = LMS(window)  # Create an instance of the LMS class
    window.mainloop()  # Start the main loop for the LMS application



