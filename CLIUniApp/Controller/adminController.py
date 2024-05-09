from Color import Color
from Database import Database
from Admin import Admin

#for dummy
import random
from Subjects import Subjects

class AdminController:
    def __init__(self, students) -> None:
        self.admin = Admin()
        self.students = students

    def showAdminMenu(self):
        # Show admin menu
        while True:
            # Get input from user
            choice = input(Color.CYAN + "\tAdmin system (c/g/p/r/s/x): " + Color.DEFAULT)    

            if choice == 'c':
                isCleared = self.admin.removeAllStudents(self.students)
                if isCleared:
                    Database.clear()
    
            elif choice == 'g':
                self.admin.viewStudentsbyGrade(self.students)

            elif choice == 'p':
                self.admin.viewStudentsbyCategories(self.students)

            elif choice == 'r':
                isRemoved = self.admin.removeStudent(self.students)
                if isRemoved:
                    Database.write(self.students)

            elif choice == 's':
                self.admin.viewStudents(self.students)

            elif choice == 'x':
                break

            #dummy purpose
            elif choice == 'd':
                for a in range(0,5):
                    self.students.append(StudentDummy())
                Database.write(self.students)
            else:
                print("\tInvalid choice. Please try again.")


class StudentDummy:
    def __init__(self) -> None:
        randStr = f"{random.randint(0, 999):03}"
        self.studentid = randStr
        self.name = 'This is name of student ' + randStr
        self.email = self.name + '@university.com'
        self.password = 'pass'
        self.subjects = []
        for a in range(0,4):
            self.subjects.append(Subjects())

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