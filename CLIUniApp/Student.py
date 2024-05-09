import json
import re
import random
import Subjects
from Color import Color


class Student:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.subjects = self.load_subjects()
        
    def showStudentMenu(self, students):
        # Show student menu
        while True:
            choice = input("Student system (l/r/x): ")
            if choice == 'l':
                email = Student.getInputEmail()
                password = Student.getInputPassword()
                student = self.findStudentByEmail(email)
                if student and student['password'] == password:
                    print(f"Welcome {student['name']}!")
                    # Show student options after successful login
                    self.showStudentCourseMenu()
                else:
                    print("Invalid credentials.")
            elif choice == 'r':
                # student registration import from Student.py
                name = Student.getInputName()
                email = Student.getInputEmail()
                password = Student.getInputPassword()
                student.registerStudent(name, email, password)
                
            elif choice == 'x':
                print('Thank you')
                break
            else:
                print("Invalid choice. Please try again.")

    def showStudentCourseMenu(self):
        while True:
            choice = input("Student Course Menu (c/e/r/s/x): ")
            if choice == 'c':
                # change
                print('3')
            elif choice == 'e':
                # enrol
                print('3')
            elif choice == 'r':
                # remove 
                print('3')
            elif choice == 's':
                # show
                print('3')
            elif choice == 'x':
                # exit
                print('3')
                break
            else:
                print("Invalid choice. Please try again.")


    def load_subjects(self):
        # Load subjects from 'students.data'
        try:
            with open('Storage/students.data', 'r') as file:
                students_data = json.load(file)
                for student in students_data:
                    if student['email'] == self.email:
                        return student['subjects']
        except FileNotFoundError:
            return []
        return []

# consider it may not be staticmethod
    @staticmethod
    def registerStudent(name, email, password):
        # Register a new student in 'students.data'
        new_student = {
            # "student_id": self.generateStudentId(),  # Generate a random student ID between 10000 and 99999
            "name": name,
            "email": email,
            "password": password,
            "subjects": []
        }  
        Student.validateEmail(new_student['email'])
        
        try:
            with open('students.data', 'r+') as file:
                students_data = json.load(file)
                students_data.append(new_student)
                file.seek(0)
                json.dump(students_data, file, indent=4)
                file.truncate()
        except FileNotFoundError:
            with open('students.data', 'w') as file:
                json.dump([new_student], file, indent=4)

    @staticmethod
    def getInputName():
        return input("Enter student's name: ")

    @staticmethod
    def getInputEmail():
        email = input("Enter student's email: ")
        while not Student.validateEmail(email):
            print("Invalid email format. Please try again.")
            email = input("Enter student's email: ")
        return email

    @staticmethod
    def validateEmail(email):
        if email is None:
            return False
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def generateStudentId(self):
        return random.randint(10000, 99999)

    def login(self):
        self.getInputEmail()
        self.getInputPassword()
        return self.verifyCredentials()

    @staticmethod
    def getInputPassword():
        return input("Enter password: ")

    def verifyCredentials(self):
        try:
            with open('students.data', 'r') as file:
                students_data = json.load(file)
                for student in students_data:
                    if student['email'] == self.email and student['password'] == self.password:
                        return True
        except FileNotFoundError:
            return False
        return False

    def findStudentByEmail(self, email):
        try:
            with open('students.data', 'r') as file:
                students_data = json.load(file)
                for student in students_data:
                    if student['email'] == email:
                        return student
        except FileNotFoundError:
            return None
        return None

    def isExistingStudent(self):
        return self.findStudentByEmail(self.email) is not None

    def enrolSubject(self, subject_name):
        # Create an instance of the Subjects class
        subject = Subjects()
        self.subjects.append({
            "subject_name": subject_name,
            "subject_id": subject.subjectID,
            "mark": subject.mark,
            "grade": subject.grade,
            "category": subject.category
        })
        self.notifyEnrolment(subject_name, subject.subjectID, subject.grade)

    def notifyEnrolment(self, subject_name, subject_id, grade):
        print(f"{self.name} has been enrolled in {subject_name} with ID {subject_id} and received a grade of {grade}.")

    def removeSubject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

    def showEnrolments(self):
        print(f"{self.name} is enrolled in the following subjects: {', '.join(self.subjects)}")

    def changePassword(self, new_password):
        self.password = new_password
        self.saveStudent()

    def saveStudent(self):
        # Update and save the registered and changed password to 'students.data'
        try:
            with open('students.data', 'r+') as file:
                students_data = json.load(file)
                for student in students_data:
                    if student['email'] == self.email:
                        student['password'] = self.password
                        student['subjects'] = self.subjects
                        break
                file.seek(0)
                json.dump(students_data, file, indent=4)
                file.truncate()
        except FileNotFoundError:
            print("Error: 'students.data' file not found.")
            
    def findStudentByEmail(self, email):
    # Find a student by email
        for student in self.students:
            if student['email'] == email:
                return student
        return None

class StudentDummy:
    def __init__(self) -> None:
        randStr = f"{random.randint(0, 999):03}"
        self.studentid = randStr
        self.name = 'This is name of student ' + randStr
        self.email = self.name + '@university.com'
        self.password = 'pass'
        self.subjects = []
        for a in range(0,4):
            self.subjects.append(Subjects.Subjects())

    def __str__(self) -> str:
        return Color.DEFAULT + f'\t{self.name} :: {self.studentid} --> Email: {self.email}' + Color.DEFAULT
    
    def studentGrade(self) -> str:
        return f'{self.name} :: {self.studentid} --> GRADE: {self.calculateGrade()} - MARK: {self.calculateMark():.2f}'
    
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
    
    def match(self, studentId):
        return self.studentid == studentId