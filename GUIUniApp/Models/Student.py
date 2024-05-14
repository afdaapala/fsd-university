import tkinter as tk
from tkinter.messagebox import showerror
import re
import os
from Models.Subject import Subject
from View.NewWindow import NewWindow
from Models.Database import Database
from Styles.Style import Colors

current_directory = os.getcwd()
filename = current_directory + "/GUIUniApp/Styles/uts.png"
class Student:
    
    def __init__(self, id, name, email, password) :
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    @staticmethod
    def findStudentByEmail(email):

        students = Database.read()
        for student in students:
            if student.email == email:
                return student
        return None

    @staticmethod
    def inputLogin(): 
        root=tk.Tk()
        root.geometry("500x500")
        root.title("Student System")
        root.configure(bg=Colors.bgColor)
        root.resizable(False, False)
        
        image=tk.PhotoImage(file=filename).subsample(20) 
        label=tk.Label(root, image=image, bg=Colors.bgColor)
        label.grid(column=1, row=1)

        box = tk.LabelFrame(root, text="Sign In", bg=Colors.bgColor, fg="white",
                            padx=20, pady=60, font='Helvetica 10 bold')
        box.columnconfigure(0, weight=1)
        box.columnconfigure(1, weight=2)
        box.place(rely=0.5, relx=0.5, anchor='center')

        emailLbl = tk.Label(box, text="Email: ", justify="left", fg="white",
                            font='Helvetica 12 bold', bg=Colors.bgColor)
        emailLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

        passwordLbl = tk.Label(box, text='Password: ', fg="white",
                              font='Helvetica 12 bold', bg=Colors.bgColor)
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

        def isValidPassword():
            password_pattern = r'^[A-Z][a-zA-Z]{5,}[0-9]{3,}$'
            return re.match(password_pattern, password.get()) is not None

        def clear():
            passwordField.delete(0, tk.END)

        def login():
            registeredStudent = Student.findStudentByEmail(email.get())
            
            if (not email.get() or not password.get()):
                info = "Empty login fields"
                showerror(title="Login Error", message = info)
                clear()
            elif registeredStudent == None:
                info = "Incorrect student credentials"
                showerror(title="Login Error", message = info)
                clear()
            elif not isValidEmail() or not isValidPassword():
                info = "Incorrect email or password format"
                showerror(title="Login Error", message = info)
                clear()   
            elif not(registeredStudent.email == email.get() and registeredStudent.password == password.get()):
                info="Student does not exist"
                showerror(title="Login Error", message = info)
                clear()
            else : 
                NewWindow(root, f"Welcome {registeredStudent.name}")      
                Student.handleSubject(registeredStudent)
                clear()   
        
        loginBtn = tk.Button(box, text="Login", command=login)
        loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        root.mainloop()
    
    @staticmethod
    def handleSubject(registeredStudent):
        root=tk.Tk()
        root.geometry("500x300")
        root.title("Enrol Subject")
        root.configure(bg=Colors.bgColor)
        root.resizable(False, False)

        enrollBtn = tk.Button(root, text="Enrol Subject", highlightbackground=Colors.enrollBtnColor, command=lambda: Student.enrollSubject(registeredStudent.subjects, root))
        enrollBtn.place(relx=0.5, rely=0.4, anchor="center", width=100, height=50)
        
        subjectBtn = tk.Button(root, text="Show Subject",highlightbackground=Colors.subjectBtnColor, command=lambda: Student.showSubjects(registeredStudent.subjects))
        subjectBtn.place(relx=0.5, rely=0.6, anchor="center", width=100, height=50)

        root.mainloop()

    @staticmethod
    def showSubjects(subjects):
        root=tk.Tk()
        root.geometry("500x300")
        root.title("Show Subject")
        root.configure(bg=Colors.bgColor)
        root.resizable(False, False)
        subjectList = tk.Listbox(root)
        
        for index, subject in enumerate(subjects):
            subjectList.insert(index, f"[ Subject:: {subject.id} -- mark = {subject.mark} -- grade = {subject.grade} ]")

        subjectList.pack(fill=tk.BOTH, expand=True, padx=20, pady=40)

        root.mainloop()
    
    @staticmethod
    def enrollSubject(subjects, root):
        if len(subjects) == 4:
            info = "Students are allowed to enrol in 4 subjects only"
            showerror(title="Confirmation", message = info)
            return None
    
        subject = Subject.generateSubject()
        subjects.append(subject)
        NewWindow(root, f"Success Enrol Subject \n You are now enrolled in {len(subjects)} out of 4 subjects")
        return subject

        

    
student = Student