from Color import Color
from Controller.studentController import StudentController
from Controller.AdminController import AdminController

class University:
    def __init__(self):
        self.studentController = StudentController()
        self.studentController.initializeStudentData()
        # Load students data
        self.students = self.studentController.readStudentData()
        self.adminController = AdminController(self.students)

    def main(self):
        # Main method to run the university system
        while True:
            choice = input(Color.CYAN + "University System: (A)dmin (S)tudent, or X: " + Color.DEFAULT)
            if choice == 'A':
                self.adminController.showAdminMenu()
            elif choice == 'S':
                pass
            elif choice == 'X':
                print(Color.YELLOW + "Thank You" + Color.DEFAULT)
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    univ = University()
    univ.main()
