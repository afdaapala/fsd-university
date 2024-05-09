from Color import Color
from Database import Database
from Admin import Admin
from Student import StudentDummy

#for dummy
import random
from Subjects import Subjects

class AdminController:
    def __init__(self) -> None:
        # Load students data
        self.admin = Admin()

    def showAdminMenu(self):
        # Show admin menu
        while True:
            # Get input from user
            choice = input(Color.CYAN + "\tAdmin system (c/g/p/r/s/x): " + Color.DEFAULT)    

            if choice == 'c':
                students = Database.read()
                isCleared = self.admin.removeAllStudents(students)
                if isCleared:
                    Database.clear()
    
            elif choice == 'g':
                students = Database.read()
                self.admin.viewStudentsbyGrade(students)

            elif choice == 'p':
                students = Database.read()
                self.admin.viewStudentsbyCategories(students)

            elif choice == 'r':
                students = Database.read()
                isRemoved = self.admin.removeStudent(students)
                if isRemoved:
                    Database.write(students)

            elif choice == 's':
                students = Database.read()
                self.admin.viewStudents(students)

            elif choice == 'x':
                break

            #dummy purpose
            elif choice == 'd':
                students = Database.read()
                for a in range(0,5):
                    students.append(StudentDummy())
                Database.write(students)

            else:
                print(Color.RED + "\tInvalid choice. Please try again." + Color.DEFAULT)
