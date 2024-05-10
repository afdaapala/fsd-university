# from Controllers.universityController import University
from Controllers.adminController import adminController
from Controllers.studentController import studentController
from Styles.Style import textColors

class University:
    def main(self):
        # Main method to run the university system
        admin = adminController()
        student = studentController()
        while True:
            choice = input(f"{textColors.CYAN} University System: (A)dmin (S)tudent, or X: {textColors.DEFAULT}")
            if choice == 'A':
                admin.showAdminMenu()
            elif choice == 'S':
                student.showStudentMenu()
            elif choice == 'X':
                print(textColors.YELLOW+'Thank you'+textColors.DEFAULT)
                break
            else:
                print(textColors.RED+"Invalid choice. Please try again."+textColors.DEFAULT)

if __name__ == "__main__":
    univ = University()
    univ.main()