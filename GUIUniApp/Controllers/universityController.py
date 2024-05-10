from Styles.Style import textColors
from Controllers.adminController import adminController
from Controllers.studentController import studentController
from Models.Database import Database

class University:
    def __init__(self):
        database = Database()
        self.students = database.load_students()  # Load student list from the student.data

    def main(self):
        # Main method to run the university system
        admin = adminController()
        student = studentController()
        while True:
            choice = input(textColors.CYAN+"University System: (A)dmin (S)tudent, or X: "+textColors.DEFAULT)
            if choice == 'A':
                admin.showAdminMenu()
            elif choice == 'S':
                student.showStudentMenu()
            elif choice == 'X':
                print(textColors.YELLOW+'Thank you'+textColors.DEFAULT)
                break
            else:
                print(textColors.RED+"Invalid choice. Please try again."+textColors.DEFAULT)
