import pickle5 as pk
import random
import re
import os
import json

class StudentController:
    @staticmethod
    def saveStudent(new_student):
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
        while not StudentController.validateEmail(email):
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