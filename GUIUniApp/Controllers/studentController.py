import pickle as pk
from Styles.Style import textColors
from Models.Student import Student
from Controllers.subjectController import subjectController
import random
import re
import os

class studentController:
    def showStudentMenu(self):
        # Show student menu
        while True:
            choice = input(f"{textColors.CYAN}\tStudent System (l/r/x): {textColors.DEFAULT}")
            if choice == 'l':
                print(f"{textColors.GREEN}\tStudent Sign In{textColors.DEFAULT}")
                while True:
                    email = input("\tEmail: ")
                    password = input("\tPassword: ")
                    if not (Student.getInputEmail(email) and Student.getInputPassword(password)):
                        print(f"{textColors.RED}\tIncorrect email or password format{textColors.DEFAULT}")
                        continue
                    elif Student.getInputEmail(email) and Student.getInputPassword(password):
                        print(f"{textColors.YELLOW}\temail and password formats acceptable{textColors.DEFAULT}")
                        findStudent = Student.findStudentByEmail(email)
                        if findStudent is None:
                            print(f"{textColors.RED}\tStudent {findStudent} does not exist{textColors.DEFAULT}")
                            break
                        else:
                            login = Student.login(email, password)
                            if login == True:
                                print(f"{textColors.GREEN}\tStudent {findStudent} logged in{textColors.DEFAULT}")
                                self.showStudentCourseMenu(findStudent, email, password)
                                break
                                
                            
                    
            elif choice == 'r':
                # student registration
                print(f"{textColors.GREEN}\tStudent Sign Up{textColors.DEFAULT}")
                while True:
                    email = input("\tEmail: ")
                    password = input("\tPassword: ")
                    if not (Student.getInputEmail(email) and Student.getInputPassword(password)):
                        print(f"{textColors.RED}\tIncorrect email or password format{textColors.DEFAULT}")
                        continue
                    elif Student.getInputEmail(email) and Student.getInputPassword(password):
                        print(f"{textColors.YELLOW}\temail and password formats acceptable{textColors.DEFAULT}")
                        findStudent = Student.findStudentByEmail(email)
                        if findStudent is not None:
                            print(f"{textColors.RED}\tStudent {findStudent} already exists{textColors.DEFAULT}")
                            break  
                        else:
                            name = input("\tName: ")
                            name = Student.getInputName(name)
                            Student.registerStudent(name, email, password)
                            print(f"{textColors.GREEN}\tEnrolling Student {name}{textColors.DEFAULT}")
                            break
                            # except:
                            #     print(f"{textColors.RED}\tFailed to enroll student {name}{textColors.DEFAULT}")
                            #     break
                            
                    
            elif choice == 'x':
                break
            else:
                print(f"{textColors.YELLOW}Invalid choice. Please try again.{textColors.DEFAULT}")

    def showStudentCourseMenu(self, name, email, password):
        currentStudent = Student(name, email, password)
        subjectView = subjectController()
        while True:
            choice = input(f"{textColors.CYAN}\t\tStudent Course Menu (c/e/r/s/x): {textColors.DEFAULT}")
            if choice == 'c':
                # change password
                print(f"{textColors.YELLOW}\t\tUpdating Password{textColors.DEFAULT}")
                while True:
                    new_password = input("\t\tNew Password: ")
                    confirm_new_password = input("\t\tConfirm New Password: ")
                    if new_password == confirm_new_password:
                        currentStudent.changePassword(new_password)
                        print(f"{textColors.YELLOW}\t\tUpdating Password{textColors.DEFAULT}")
                        break
                    else:
                        print(f"{textColors.RED}\t\tPasswords does not match - try again{textColors.DEFAULT}")
                        continue
                
            elif choice == 'e':
                # enroll 1 subject
                subjectView.enrolSubject(currentStudent)
            elif choice == 'r':
                # remove subject by id
                subjectView.removeSubject(currentStudent)
            elif choice == 's':
                # show subjects
                subjectView.showEnrolledSubjectList(currentStudent)
                
            elif choice == 'x':
                # exit
                break
            else:
                print("Invalid choice. Please try again.")
    