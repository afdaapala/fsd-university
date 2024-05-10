import re
import random
from Controller.StudentController import StudentController as controller
from Controller.SubjectController import SubjectController
from Subject import Subject


class Student:
    # Email regex pattern
    email_pattern = r'^[a-z]+\.+[a-z]+@university\.com$'
    
    # Password regex pattern
    password_pattern = r'^[A-Z][a-zA-Z]{5,}[0-9]{3,}$'
    
    def __init__(self, student):
        self.id = student['id']
        self.name = student['name']
        self.email = student['email']
        self.password = student['password']
        self.subjects = self.formatSubjects(student['subjects'])
    
    ### start 
    
    # check if the student id exists
    @staticmethod
    def isExistingId(id):
        for student in controller.read():
            if student['id'] == id:
                return True
        return False
    
    @staticmethod
    def generateId():
        newStudentId = str(random.randint(1, 999999)).rjust(6, '0')
        if Student.isExistingId(newStudentId):
            return Student.generateId()
        return newStudentId
    
    
    # Show student menu
    @staticmethod
    def showStudentMenu():
        while True:
            choice = input("\033[34mStudent system (l/r/x): \033[0m")
            if choice == 'l':
                Student.login()
            elif choice == 'r':
                Student.registerStudent()
            elif choice == 's':
                print(controller.read())    
            
            elif choice == 'x':
                print('Thank you')
                break
            else:
                print("Invalid choice. Please try again.")

    def showStudentCourseMenu(self):
        while True:
            choice = input("\033[34mStudent Course Menu (c/e/r/s/x): \033[0m")
            if choice == 'c':
                # change
                self.changePassword()
            elif choice == 'e':
                # enrol
                self.enrollSubject()
            elif choice == 'r':
                # remove 
                self.removeSubject()
            elif choice == 's':
                # show
                self.showSubjects()
            elif choice == 'x':
                # exit
                break
            else:
                print("Invalid choice. Please try again.")
       
    # Register a new student in 'students.data'
    @staticmethod         
    def registerStudent():
        print("\033[32mStudent Sign Up\033[0m")

        email = input("Email: ")
        password = input("Password: ")

        while(not (Student.isValidEmail(email) and Student.isValidPassword(password))):
            print("\033[31mIncorrect email or password format\033[0m")
            email = input("Email: ")
            password = input("Password: ")

        print(f"\033[33memail and password formats aceeptable\033[0m")

        registeredStudent = controller.findStudentByEmail(email)
        if registeredStudent != None:
            print(f"\033[31mStudent {str(registeredStudent['name']).title()} already exists\033[0m")
        else:
            name = input("Name: ")
            print(f"\033[33mEnrolling Student {name}\033[0m")
            controller.registerStudent({
                "id": Student.generateId(),
                "email": email,
                "password": password,
                "name": name,
                "subjects": []
            })

    # Function to check if the email is valid
    @staticmethod
    def isValidEmail(email):
        return re.match(Student.email_pattern, email) is not None

    # Function to check if the password is valid
    @staticmethod
    def isValidPassword(password):
        return re.match(Student.password_pattern, password) is not None
    
    @staticmethod
    def login():
        print("\033[32mStudent Sign In\033[0m")
        
        email = input("Email: ")
        password = input("Password: ")

        while(not (Student.isValidEmail(email) and Student.isValidPassword(password))):
            print("\033[31mIncorrect email or password format\033[0m")
            email = input("Email: ")
            password = input("Password: ")

        print(f"\033[33memail and password formats aceeptable\033[0m")
        
        registeredStudent = controller.findStudentByEmail(email)
        if registeredStudent == None:
            print(f"\033[31mStudent does not exist\033[0m")
        else:
            if registeredStudent['password'] != password:
                print(f"\033[31mStudent does not exist\033[0m")
            else :
                Student(registeredStudent).showStudentCourseMenu()
            
    def showSubjects(self):
        print(f"\033[33mShowing {len(self.subjects)} subjects\033[0m")
        for subject in self.subjects:
            print(f"[ Subject:: {subject.id} -- mark = {subject.mark} -- grade = {subject.grade} ]\n")
    
    def enrollSubject(self):
        if len(self.subjects) == 4:
            print("\033[31mStudents are allowed to enrol in 4 subjects only\033[0m")
            return
    
        subject = Subject.generateSubject()
        print(f"\033[33mEnrolling in Subject-{subject.id}\033[0m")
        self.subjects.append(subject)
        SubjectController.enrollSubject(self.id, subject)

        print(f"\033[33mYou are now enrolled in {len(self.subjects)} out of 4 subjects\033[0m")
            
    def formatSubjects(self, subjects):
        newSubjects = []
        for subject in subjects:
            newSubjects.append(Subject(subject['id'], subject['mark'], subject['grade']))
        return newSubjects
    
    def isPass(self):
        return self.getAverageMark() >= 50
    
    def getAverageMark(self):
        total = 0
        for subject in self.subjects:
            total += subject.mark
        return total / len(self.subjects)
    
    def removeSubject(self):
        if len(self.subjects) == 0:
            return
        
        removeSubject = self.subjects.pop()
        print(f"Remove Subject by ID: {removeSubject.id}")
        print(f"\033[33mDroping Subject-{removeSubject.id}\033[0m")
        SubjectController.removeSubject(self.id, removeSubject)
        
        print(f"\033[33mYou are now enrolled in {len(self.subjects)} out of 4 subjects\033[0m")
        
    
    def changePassword(self):
        print(f"\033[33mUpdating Password\033[0m")

        newPassword = input('New Password: ')
        while(not (Student.isValidPassword(newPassword))):
            print("\033[31mIncorrect password format\033[0m")
            newPassword = input("New Password: ")

        newPasswordConfirm = input('Confirm Password: ')
        
        while(newPassword != newPasswordConfirm):
            print("\033[31mPasswords does not match - try again\033[0m")
            newPasswordConfirm = input('Confirm Password: ')
            
        self.password = newPassword
        controller.changePassword(self.id, newPassword)
        
