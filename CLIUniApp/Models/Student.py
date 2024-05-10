import pickle as pk
import re
import random
import Models.Subjects as Subjects
from Models.Database import Database


class Student:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        # self.subjects = self.load_subjects()
        self.subjects = []

    def load_subjects(self):
        # Load subjects from 'Storage/students.data'
        try:
            with open('Storage/students.data', 'rb') as file:
                students = pk.load(file)
                for student in students:
                    if student['email'] == self.email:
                        return student['subjects']
        except FileNotFoundError:
            return []
        return []
    
    def changePassword(self, new_password):
        database = Database()
        students = database.load_students()
        for student in students:
            if student['email'] == self.email:
                student['password'] = new_password
                database.save_student(student)
                return True
        
    
    @staticmethod
    def registerStudent(name, email, password):
        # Register a new student in 'students.data'
        database = Database()
        new_student = {
            # "student_id": self.generateStudentId(),  # Generate a random student ID between 10000 and 99999
            "name": name,
            "id": Student.generateStudentId(),
            "email": email,
            "password": password,
            "subjects": []
        }
        database.save_student(new_student)     

    @staticmethod          
    def getInputName(name_input):
        name = name_input.title()
        return name

    @staticmethod
    def getInputEmail(email_input):
        email = Student.validateEmail(email_input)
        if email is False:
            return False
        return email
        
    @staticmethod
    def validateEmail(email):
        valid_email = re.match(r"^[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+@university.com", email)
        if valid_email == None:
            return False
        return email
        
    @staticmethod   
    def generateStudentId():
        return random.randint(100000, 999999)

    @staticmethod
    def login(email, password):
        database = Database()
        students = database.load_students()
        exist_student = [student for student in students if student['email'] == email and student['password'] == password]
        if exist_student:
            return True
        else:
            return False

    @staticmethod
    def getInputPassword(password_input):
        valid_password = re.match(r"^[A-Z]{1,}(?=.*[a-z])[A-Za-z]{6,}(\d{3,})$", password_input)
        if valid_password == None:
            return False
        return password_input

    @staticmethod
    def verifyCredentials(email, password):
        try:
            database = Database()
            students = database.load_students()
            for student in students:
                if student['email'] == email and student['password'] == password:
                    return True
            return False
        except:
            return False

    @staticmethod
    def findStudentByEmail(email):
        database = Database()
        students = database.load_students()
        for student in students:
            if student['email'] == email:
                return student['name']
        return None
        

    def isExistingStudent(self):
        return self.findStudentByEmail(self.email) is not None

    # def enrolSubject(self, subject_name):
    #     # Create an instance of the Subjects class
    #     subject = Subjects()
    #     self.subjects.append({
    #         "subject_name": subject_name,
    #         "subject_id": subject.subjectID,
    #         "mark": subject.mark,
    #         "grade": subject.grade,
    #         "category": subject.category
    #     })
    #     self.notifyEnrolment(subject_name, subject.subjectID, subject.grade)

    # def notifyEnrolment(self, subject_name, subject_id, grade):
    #     print(f"{self.name} has been enrolled in {subject_name} with ID {subject_id} and received a grade of {grade}.")

    # def removeSubject(self, subject):
    #     if subject in self.subjects:
    #         self.subjects.remove(subject)

    # def showEnrolments(self):
    #     print(f"{self.name} is enrolled in the following subjects: {', '.join(self.subjects)}")

