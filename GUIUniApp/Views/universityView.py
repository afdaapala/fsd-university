import tkinter as tk
import tkinter.messagebox as mb
from Controllers.universityController import University
from Views.adminView import AdminView
from Views.studentView import StudentView

class University(tk.LabelFrame):
    def __init__(self, master, model) -> None:
        super().__init__(master)
        self.model = model
        box = tk.Frame(self, bg="light blue", bd=10)
        box.place(x=10, y=10, width=500, height=680)
        
        adminButton = tk.Button(box, text="Admin", command=self.adminButtonClicked)
        studentButton = tk.Button(box, text="Student", command=self.studentButtonClicked)
        exitButton = tk.Button(box, text="Exit", command=self.exitButtonClicked)
        
        adminButton.place(x=10, y=10, width=100, height=50)
        studentButton.place(x=10, y=120, width=100, height=50)
        exitButton.place(x=10, y=230, width=100, height=50)
        
    def adminButtonClicked(self):
        admin = AdminView(self)
        admin.pack(fill="both", expand=True)
    
    def studentButtonClicked(self):
        student = StudentView(self, self.model)
        student.pack(fill="both", expand=True)
        
    def exitButtonClicked(self):
        if mb.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.quit()