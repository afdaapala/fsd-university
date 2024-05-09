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
        self.students = Database.read()
        self.admin = Admin()

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
                print(Color.RED + "\tInvalid choice. Please try again." + Color.DEFAULT)
