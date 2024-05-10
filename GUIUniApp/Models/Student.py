import tkinter as tk
from tkinter.messagebox import showerror
import re
from Models.Subject import Subject
from Styles.NewWindow import NewWindow
from Models.Database import Database

class StudentGUI:
    def __init__(self, id, name, email, password) :
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

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
        print("students>>>>",students)
        for student in students:
            if student.email == email:
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
        
        print(">>>>>>>>>>",email, email.get())
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
            print("email:", email, email.get())
            registeredStudent = StudentGUI.findStudentByEmail(email.get())
            print("registeredStudent: ", registeredStudent)
            if(not email.get() and not password.get()):
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
        print("show subject")
        # root=tk.Tk()
        # root.geometry("500x300")
        # root.title("Enrol Subject")
        # root.configure(bg="#323232")
        # root.resizable(False, False)
        # subjects = self.subjects
        # listVar = tk.Variable(value=subjects)
        # subjectList = tk.Listbox(root, listvariable=listVar)
        # subjectList.pack(fill=tk.BOTH, expand=True, padx=20, pady=40)

        # root.mainloop()

    def enrollSubject(self):
        if len(self.subjects) == 4:
            info = "Students are allowed to enrol in 4 subjects only"
            showerror(title="Confirmation", message = info)
            return None
    
        subject = Subject.generateSubject()
        self.subjects.append(subject)

        return subject

        

    
student = StudentGUI