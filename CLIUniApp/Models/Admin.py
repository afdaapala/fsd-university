from Models.Database import Database
import pickle

class Admin:
    def __init__(self):
        pass
    
    def viewStudents(self):
        # view all students from the database Storage/students.data
        database = Database()
        students = database.load_students()
        return students
        

    def viewStudentsbyGrade(self):
        # view students by grade
        database = Database()
        students = database.load_students()
        Fgroupstudent = []
        Pgroupstudent = []
        Cgroupstudent = []
        Dgroupstudent = []
        HDgroupstudent = []
        for student in students:
            if student['grade'] == 'F':
                Fgroupstudent.append(student)
            elif student['grade'] == 'P':
                Pgroupstudent.append(student)
            elif student['grade'] == 'C':
                Cgroupstudent.append(student)
            elif student['grade'] == 'D':
                Dgroupstudent.append(student)
            elif student['grade'] == 'HD':
                HDgroupstudent.append(student)

        return Fgroupstudent, Pgroupstudent, Cgroupstudent, Dgroupstudent, HDgroupstudent

    def viewStudentsbyCategories(self):
        # view students by categories
        database = Database()
        students = database.load_students()
        passGroupStudent = [] 
        failGroupStudent = []
        for student in students:
            if student['grade'] == 'F':
                failGroupStudent.append(student)
            else:
                passGroupStudent.append(student)
                
        return passGroupStudent, failGroupStudent

    def removeStudent(self, student_id):
        database = Database()
        # remove student from the database
        database.removeStudent(student_id)

    def removeAllStudents(self):
        database = Database()
        # remove all students from the database
        database.clearAllData()
