import hashlib
class Admin:
    def __init__(self):
        self.__admin_email = "admin@example.com"
        self.__admin_password = self.hashPassword("admin123")

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
