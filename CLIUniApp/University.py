from Admin import Admin
from Student import Student

class University:
    def __init__(self):
        self.students = []  # Load student list from the student.data

    def main(self):
        # Main method to run the university system
        admin = Admin()

        while True:
            choice = input("University System: (A)dmin (S)tudent, or X: ")
            if choice == 'A':
                admin.showAdminMenu()
            elif choice == 'S':
                Student.showStudentMenu()
            elif choice == 'X':
                print('Thank you')
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    univ = University()
    univ.main()
