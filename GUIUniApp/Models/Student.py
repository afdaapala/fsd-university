import tkinter as tk
from tkinter import messagebox
import re

class StudentGUI:
    def __init__(self):
      # Email regex pattern
      self.email_pattern = r'^[a-z]+\.+[a-z]+@university\.com$'
      
      # Password regex pattern
      self.password_pattern = r'^[A-Z][a-zA-Z]{5,}[0-9]{3,}$'

    @staticmethod
    def viewMenu():
        root=tk.Tk()
        root.geometry("500x200")
        root.title("Student System")
        root.configure(bg="#323232")
        root.resizable(False, False)

        label = tk.Label(root, text="Student system",
                        fg="white", font="Helvetica 18 bold",
                        padx=20, pady=20)
        label.pack()

        btn = tk.Button(root, text="l(ogin)", font='Helvetica 14 bold', command=StudentGUI.inputLogin)
        btn.pack()

        btn = tk.Button(root, text="r(egister)", font='Helvetica 14 bold')
        btn.pack()

        btn = tk.Button(root, text="x(exit)", font='Helvetica 14 bold', command=lambda: root.quit())
        btn.pack()

        root.mainloop()

    @staticmethod
    def inputLogin(): 
        root=tk.Tk()
        root.geometry("500x200")
        root.title("Student System")
        root.configure(bg="#323232")
        root.resizable(False, False)

        box = tk.LabelFrame(root, text="Sign In", bg="#323232", fg="white",
                            padx=20, pady=20, font='Helvetica 10 bold')
        box.columnconfigure(0, weight=1)
        box.columnconfigure(1, weight=2)
        box.place(rely=0.5, relx=0.5, anchor='center')

        emailLbl = tk.Label(box, text="Email: ", justify="left", fg="white",
                            font='Helvetica 12 bold', bg="#323232")
        emailLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

        passwordLbl = tk.Label(box, text='Password: ', fg="white",
                              font='Helvetica 12 bold', bg="#323232")
        passwordLbl.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

        emailText = tk.StringVar()
        emailField = tk.Entry(box, textvariable=emailText)
        emailField.grid(column=1, row=0, padx=5, pady=5)
        emailField.focus()

        passwordTxt = tk.StringVar()
        passwordField = tk.Entry(box, textvariable=passwordTxt, show="*")
        passwordField.grid(column=1, row=1, padx=5, pady=5)

        cancelBtn = tk.Button(box, text="Cancel", command=lambda: root.destroy())
        cancelBtn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)


        def login():
           print("login success")
        
        loginBtn = tk.Button(box, text="Login", command=login)
        loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        root.mainloop()
  
        # registered_student = Student.find_student_by_email(email)
        # if registered_student is None:
        #     messagebox.showerror("Error", "Student does not exist")
        #     return
        # else:
        #     if registered_student['password'] != password:
        #         messagebox.showerror("Error", "Incorrect password")
        #         return
        #     else:
        #         messagebox.showinfo("Success", "Login successful!")
        #         # Call your next function here, e.g., show_subjects()

    def register(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not (self.is_valid_email(self, email) and self.is_valid_password(password)):
            messagebox.showerror("Error", "Incorrect email or password format")
            return

        name = input("Name: ")  # You can add a name entry in the GUI as well
        # Student.register_student({
        #     "id": Student.generate_id(),
        #     "email": email,
        #     "password": password,
        #     "name": name,
        #     "subjects": []
        # })
        messagebox.showinfo("Success", "Registration successful!")

    def change_password(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not (self.is_valid_email(self, email) and self.is_valid_password(self, password)):
            messagebox.showerror("Error", "Incorrect email or password format")
            return

        new_password = input("New Password: ")  # You can add a new password entry in the GUI as well
        if not self.is_valid_password(self, new_password):
            messagebox.showerror("Error", "Incorrect password format")
            return

        new_password_confirm = input('Confirm Password: ')
        if new_password != new_password_confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return

        # Student.change_password(email, new_password)
        messagebox.showinfo("Success", "Password changed successfully!")

    @staticmethod
    def is_valid_email(self, email):
        return re.match(self.email_pattern, email) is not None

    @staticmethod
    def is_valid_password(self, password):
        return re.match(self.password_pattern, password) is not None

    
student = StudentGUI