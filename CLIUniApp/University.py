import Admin
import Student
import Subjects
import json

class University:
    def __init__(self):
        self.admins = self.load_admins()  # Load admin list from a file or define here
        self.students = self.load_students()  # Load student list from the student.data

    def load_admins(self):
        # Load admins from a file (assuming 'admins.data' is a JSON file)
        try:
            with open('admins.data', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist

    def load_students(self):
        # Load students from 'students.data'
        try:
            with open('students.data', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist

    def main(self):
        # Main method to run the university system
        while True:
            print(f"Welcome to the University System!")
            print("1. Student Menu")
            print("2. Admin Menu")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.showStudentMenu()
            elif choice == '2':
                self.showAdminMenu()
            elif choice == '3':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

    def showStudentMenu(self):
        # Show student menu
        print("Student Menu")
        print("1. Login")
        print("2. Register")
        print("3. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            email = Student.Student.getInputEmail()
            password = Student.Student.getInputPassword()
            student = self.findStudentByEmail(email)
            if student and student['password'] == password:
                print(f"Welcome {student['name']}!")
                # Show student options after successful login
            else:
                print("Invalid credentials.")
        elif choice == '2':
            # student registration import from Student.py
            name = Student.Student.getInputName()
            email = Student.Student.getInputEmail()
            password = Student.Student.getInputPassword()
            student = Student.Student(name, email, password)
            student.registerStudent(name, email, password)
            
        elif choice == '3':
            return
        else:
            print("Invalid choice. Please try again.")

    def showAdminMenu(self):
        # Show admin menu
        print("Admin Menu")
        print("1. Login")
        print("2. View Students")
        print("3. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            email = input("Enter admin email: ")
            password = input("Enter admin password: ")
            admin = self.findAdminByEmail(email)
            if admin and admin['password'] == password:
                print("Admin login successful.")
                # Show admin options after successful login
            else:
                print("Invalid credentials.")
        elif choice == '2':
            # Handle viewing students
            pass
        elif choice == '3':
            return
        else:
            print("Invalid choice. Please try again.")

    def findStudentByEmail(self, email):
        # Find a student by email
        for student in self.students:
            if student['email'] == email:
                return student
        return None

    def findAdminByEmail(self, email):
        # Find an admin by email
        for admin in self.admins:
            if admin['email'] == email:
                return admin
        return None

if __name__ == "__main__":
    univ = University()
    univ.main()
