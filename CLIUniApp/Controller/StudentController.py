# import pickle
from Database import Database


class StudentController:
    @staticmethod
    def read():
        return Database.read()
            
    @staticmethod
    def findStudentByEmail(email):
        students = Database.read()
        for student in students:
            if student['email'] == email:
                return student
        return None
    
    @staticmethod
    def registerStudent(student):
        students = Database.read()
        students.append(student)
        Database.write(students)
        
    @staticmethod
    def changePassword(id, newPassword):
        students = StudentController.read()
        print(id, newPassword, '\n', students)
        for student in students:
            if student['id'] == id:
                student['password'] = newPassword
                break
        Database.write(students)
            