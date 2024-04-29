import hashlib

class Admin:
    def __init__(self):
        self.__admin_email = "admin@example.com"
        self.__admin_password = self.hashPassword("admin123")

    def showAdminMenu(self):
        # Show admin menu
        while True:
            choice = input("Admin system (c/g/p/r/s/x): ")
            if choice == 'c':
                print("d")
                # clear database file
            elif choice == 'g':
                print("d")
                # group students
            elif choice == 'p':
                print("d")
                # partition students
            elif choice == 'r':
                print("d")
                    # remove student
            elif choice == 's':
                print("d")
                # show
            elif choice == 'x':
                break
            else:
                print("Invalid choice. Please try again.")


    def getInputEmail(self):
        return input("Enter admin email: ")

    def getInputPassword(self):
        return input("Enter admin password: ")

    def login(self):
        email = self.getInputEmail()
        password = self.getInputPassword()
        if self.verifyCredentials(email, password):
            print("Admin login successful.")
        else:
            print("Invalid admin credentials.")

    def verifyCredentials(self, email, password):
        return self.__admin_email == email and self.__admin_password == self.hashPassword(password)

    def viewStudents(self):
        print("Viewing students...")
        

    def viewStudentsbyGrade(self):
        print("Viewing students by grade...")

    def viewStudentsbyCategories(self):
        print("Viewing students by categories...")

    def removeStudent(self, student):
        print(f"Removing student {student.name}...")

    def removeAllStudents(self):
        print("Removing all students...")

    def hashPassword(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
