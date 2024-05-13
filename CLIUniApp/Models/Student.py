import re
import random
from Models.Subject import Subject
from Models.Database import Database
from Styles.Style import textColors

class Student:
    # Email regex pattern
    email_pattern = r'^[a-z]+\.+[a-z]+@university\.com$'
    
    # Password regex pattern
    password_pattern = r'^[A-Z][a-zA-Z]{5,}[0-9]{3,}$'
    
        
    def __init__(self, id, name, email, password) :
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []
    
    @staticmethod
    def isExistingId(id):
        for student in Database.read():
            if student.id == id:
                return True
        return False
    
    @staticmethod
    def generateId():
        newStudentId = str(random.randint(1, 999999)).rjust(6, '0')
        if Student.isExistingId(newStudentId):
            return Student.generateId()
        return newStudentId
        
    @staticmethod
    def registerStudent():
        print(f"{textColors.GREEN}\tStudent Sign Up{textColors.DEFAULT}")

        email = input("\tEmail: ")
        password = input("\tPassword: ")

        while(not (Student.isValidEmail(email) and Student.isValidPassword(password))):
            print(f"{textColors.RED}\tIncorrect email or password format{textColors.DEFAULT}")
            email = input("\tEmail: ")
            password = input("\tPassword: ")

        print(f"{textColors.YELLOW}\temail and password formats acceptable{textColors.DEFAULT}")

        registeredStudent = Student.findStudentByEmail(email)
        if registeredStudent != None:
            print(f"{textColors.RED}\tStudent {str(registeredStudent.name).title()} already exists{textColors.DEFAULT}")
        else:
            name = input("\tName: ")
            print(f"{textColors.YELLOW}\tEnrolling Student {name}{textColors.DEFAULT}")
            Student.insertRegisterStudent(Student(Student.generateId(), name, email, password))
            
    @staticmethod
    def findStudentByEmail(email):
        students = Database.read()
        for student in students:
            if student.email == email:
                return student
        return None

    @staticmethod
    def insertRegisterStudent(student):
        students = Database.read()
        students.append(student)
        Database.write(students)

    @staticmethod
    def updatePassword(id, newPassword):
        students = Database.read()
        for student in students:
            if student.id == id:
                student.password = newPassword
                break
        Database.write(students)
    
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
        print(f"{textColors.GREEN}\tStudent Sign In{textColors.DEFAULT}")
        
        email = input("\tEmail: ")
        password = input("\tPassword: ")

        while(not (Student.isValidEmail(email) and Student.isValidPassword(password))):
            print(f"{textColors.RED}\tIncorrect email or password format{textColors.DEFAULT}")
            email = input("\tEmail: ")
            password = input("\tPassword: ")

        print(f"{textColors.YELLOW}\temail and password formats acceptable{textColors.DEFAULT}")
        
        registeredStudent = Student.findStudentByEmail(email)
        if registeredStudent == None:
            print(f"{textColors.RED}\tStudent does not exist{textColors.DEFAULT}")
        else:
            if registeredStudent.password != password:
                print(f"{textColors.RED}\tStudent does not exist{textColors.DEFAULT}")
            else :
                return registeredStudent

    def showSubjects(self):
        print(f"{textColors.YELLOW}\t\tShowing {len(self.subjects)} subjects{textColors.DEFAULT}")
        for subject in self.subjects:
            print(f"\t\t[ Subject::{subject.id} -- mark = {subject.mark} -- grade =  {' ' if subject.grade != 'HD' else ''}{subject.grade} ]")
    
    def enrollSubject(self):
        if len(self.subjects) == 4:
            print(f"{textColors.RED}\t\tStudents are allowed to enrol in 4 subjects only{textColors.DEFAULT}")
            return None
    
        subject = Subject.generateSubject()
        print(f"{textColors.YELLOW}\t\tEnrolling in Subject-{subject.id}{textColors.DEFAULT}")
        self.subjects.append(subject)

        print(f"{textColors.YELLOW}\t\tYou are now enrolled in {len(self.subjects)} out of 4 subjects{textColors.DEFAULT}")

        return subject
    
    def isPass(self):
        return self.getAverageMark() >= 50
    
    def getAverageMark(self):
        total = 0
        for subject in self.subjects:
            total += subject.mark
        return total / len(self.subjects)
    
    def removeSubject(self):
        if len(self.subjects) == 0:
            print(f"{textColors.YELLOW}\t\tThere is no subject to remove{textColors.DEFAULT}")
            return
        
        removeSubject = self.subjects.pop()
        print(f"\t\tRemove Subject by ID: {removeSubject.id}")
        print(f"{textColors.YELLOW}\t\tDropping Subject-{removeSubject.id}{textColors.DEFAULT}")
        
        print(f"{textColors.YELLOW}\t\tYou are now enrolled in {len(self.subjects)} out of 4 subjects{textColors.DEFAULT}")
        return removeSubject
    
    def changePassword(self):
        print(f"{textColors.YELLOW}\t\tUpdating Password{textColors.DEFAULT}")

        newPassword = input('\t\tNew Password: ')
        while(not (Student.isValidPassword(newPassword))):
            print(f"{textColors.RED}\t\tIncorrect password format{textColors.DEFAULT}")
            newPassword = input("\t\tNew Password: ")

        newPasswordConfirm = input('\t\tConfirm Password: ')
        
        while(newPassword != newPasswordConfirm):
            print(f"{textColors.RED}\t\tPasswords does not match - try again{textColors.DEFAULT}")
            newPasswordConfirm = input('\t\tConfirm Password: ')
            
        self.password = newPassword
        Student.updatePassword(self.id, newPassword)
        
    def __str__(self) -> str:
        return textColors.DEFAULT + f'\t{self.name} :: {self.id} --> Email: {self.email}' + textColors.DEFAULT
    
    def studentGrade(self) -> str:
        return f'{self.name} :: {self.id} --> GRADE: {self.calculateGrade()} - MARK: {self.calculateMark():.2f}'
    
    def calculateGrade(self) -> str:
        grade = '-'
        averageMark = self.calculateMark()
        if averageMark < 50:
            grade = 'Z'
        elif averageMark >= 50 and averageMark < 65:
            grade = 'P'
        elif averageMark >= 65 and averageMark < 75:
            grade = 'C'
        elif averageMark >= 75 and averageMark < 85:
            grade = 'D'
        elif averageMark >= 85:
            grade = 'HD'
        return grade

    def calculateMark(self) -> int:
        total = 0
        average = 0
        if self.subjects != None and self.subjects.__len__() > 0:
            for subject in self.subjects:
                total += subject.mark
            average = total / self.subjects.__len__()
        return average
    
    def match(self, id):
        return self.id == id