from Styles.Style import textColors
from Models.Admin import Admin
from Models.Database import Database

# admin controller to handle user request no need to login
class adminController:
    def __init__(self):
        pass

    def showAdminMenu(self):
        admin = Admin()
        students = Database.read()
        # Show admin menu
        while True:
            choice = input(textColors.CYAN + "\tAdmin system (c/g/p/r/s/x): " + textColors.DEFAULT)
            if choice == 'c':
                # clear all students from the database
                isCleared = admin.removeAllStudents(students)
                if isCleared:
                    Database.clear()
            elif choice == 'g':
                # group students by grade
                students = Database.read()
                admin.viewStudentsbyGrade(students)
            elif choice == 'p':
                # partition students by categories
                admin.viewStudentsbyCategories(students)       
            elif choice == 'r':
                # Remove student
                isRemoved = admin.removeStudent(students)
                if isRemoved:
                    Database.write(students)
                
            elif choice == 's':
                # Student List
                # students = Database.read()
                admin.viewStudents(students)
                
            elif choice == 'x':
                break
            else:
                print(textColors.RED + "\tInvalid choice. Please try again." + textColors.DEFAULT)