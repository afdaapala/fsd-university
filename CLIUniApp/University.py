from Color import Color
from Controller.studentController import StudentController
from Controller.AdminController import AdminController
from Database import Database

class University:
    def __init__(self):
        Database.initialize()
        self.adminController = AdminController()

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
                print(Color.RED + "Invalid choice. Please try again." + Color.DEFAULT)

if __name__ == "__main__":
    univ = University()
    univ.main()
