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
            choice = input(textColors.cyan+"University System: (A)dmin (S)tudent, or X: "+textColors.reset)
            if choice == 'A':
                admin.showAdminMenu()
            elif choice == 'S':
                student.showStudentMenu()
            elif choice == 'X':
                print(textColors.yellow+'Thank you'+textColors.reset)
                break
            else:
                print(textColors.red+"Invalid choice. Please try again."+textColors.reset)
