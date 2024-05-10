import pickle as pk
from Styles.Style import textColors
from Models.Student import Student
from Models.Database import Database
from Controllers.subjectController import subjectController

class studentController:
    @staticmethod
    def showStudentMenu():
        while True:
            choice = input(f"{textColors.CYAN}\tStudent system (l/r/x): {textColors.DEFAULT}")
            if choice == 'l':
                student = Student.login()
                if student is not None:
                    studentController.showStudentCourseMenu(student)
                    
            elif choice == 'r':
                Student.registerStudent()
            elif choice == 'x':
                break
            else:
                print(f"{textColors.RED}\tInvalid choice. Please try again.{textColors.DEFAULT}")

    @staticmethod
    def showStudentCourseMenu(student):
        while True:
            choice = input(f"{textColors.CYAN}\t\tStudent Course Menu (c/e/r/s/x): {textColors.DEFAULT}")
            if choice == 'c':
                # change
                student.changePassword()
            elif choice == 'e':
                # enrol
                subject = student.enrollSubject()
                if subject is not None:
                    subjectController.enrollSubject(student.id, subject)
            elif choice == 'r':
                # remove 
                removeSubject = student.removeSubject()
                if removeSubject is not None:
                    subjectController.removeSubject(student.id, removeSubject)

            elif choice == 's':
                # show
                student.showSubjects()
            elif choice == 'x':
                # exit
                break
            else:
                print(f"{textColors.RED}\t\tInvalid choice. Please try again.{textColors.DEFAULT}")