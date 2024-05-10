import tkinter as tk
# from Controllers.adminController import Admin

class AdminView(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(text="Admin View")

        self.view_all_students_button = tk.Button(self, text="View All Students", command=self.view_all_students)
        self.view_all_students_button.pack()

        self.exit_button = tk.Button(self, text="Exit", command=self.exit)
        self.exit_button.pack()

    def view_all_students(self):
        # Code to view all students
        box = tk.Toplevel(self)
        box.title("All Students")
        box.geometry("300x400")
        box.resizable(False, False)
        

    def exit(self):
        self.master.destroy()