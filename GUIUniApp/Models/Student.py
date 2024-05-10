import tkinter as tk
from tkinter.messagebox import showerror
import re
from Models.Subject import Subject
from Styles.NewWindow import NewWindow
from Models.Database import Database

class StudentGUI:
    def __init__(self, student):
        self.id = student['id']
        self.name = student['name']
        self.email = student['email']
        self.password = student['password']
        self.subjects = self.formatSubjects(student['subjects'])

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
    def findStudentByEmail(email):
        students = Database.read()
        for student in students:
            if student['email'] == email:
                return student
        return None

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

        email = tk.StringVar()
        emailField = tk.Entry(box, textvariable=email)
        emailField.grid(column=1, row=0, padx=5, pady=5)
        emailField.focus()

        password = tk.StringVar()
        passwordField = tk.Entry(box, textvariable=password, show="*")
        passwordField.grid(column=1, row=1, padx=5, pady=5)

        cancelBtn = tk.Button(box, text="Cancel", command=lambda: root.destroy())
        cancelBtn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
        
        
        def isValidEmail():
            email_pattern = r'^[a-z]+\.+[a-z]+@university\.com$'
            return re.match(email_pattern, email.get()) is not None

        # def isValidPassword():
        #     password_pattern = r'^[A-Z][a-zA-Z]{5,}[0-9]{3,}$'
        #     return re.match(password_pattern, password.get()) is not None

        def clear():
            emailField.delete(0, tk.END)
            passwordField.delete(0, tk.END)

        def login():
            registeredStudent = StudentGUI.findStudentByEmail(email)
            
            if(not email and not password):
                info = "Empty login fields"
                showerror(title="Login Error", message = info)
                clear()
            elif registeredStudent == None:
                info = "Incorrect student credentials"
                showerror(title="Login Error", message = info)
                clear()
            elif (isValidEmail()):
                info = "Incorrect email format"
                showerror(title="Login Error", message = info)
                clear()     
            else : 
                StudentGUI.showSubjects()
                NewWindow(root, "Correct email or password")      
                clear()   
        
        loginBtn = tk.Button(box, text="Login", command=login)
        loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        root.mainloop()
        
    @staticmethod
    def showSubjects(self):
        root=tk.Tk()
        root.geometry("500x300")
        root.title("Enrol Subject")
        root.configure(bg="#323232")
        root.resizable(False, False)
        subjects = self.subjects
        listVar = tk.Variable(value=subjects)
        subjectList = tk.Listbox(root, listvariable=listVar)
        subjectList.pack(fill=tk.BOTH, expand=True, padx=20, pady=40)

        root.mainloop()

    def enrollSubject(self):
        if len(self.subjects) == 4:
            info = "Students are allowed to enrol in 4 subjects only"
            showerror(title="Confirmation", message = info)
            return None
    
        subject = Subject.generateSubject()
        self.subjects.append(subject)

        return subject

        

    
student = StudentGUI