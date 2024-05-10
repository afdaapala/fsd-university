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
            choice = input(f"{textColors.cyan}\tStudent System (l/r/x): {textColors.reset}")
            if choice == 'l':
                print(f"{textColors.green}\tStudent Sign In{textColors.reset}")
                while True:
                    email = input("\tEmail: ")
                    password = input("\tPassword: ")
                    if not (Student.getInputEmail(email) and Student.getInputPassword(password)):
                        print(f"{textColors.red}\tIncorrect email or password format{textColors.reset}")
                        continue
                    elif Student.getInputEmail(email) and Student.getInputPassword(password):
                        print(f"{textColors.yellow}\temail and password formats acceptable{textColors.reset}")
                        findStudent = Student.findStudentByEmail(email)
                        if findStudent is None:
                            print(f"{textColors.red}\tStudent {findStudent} does not exist{textColors.reset}")
                            break
                        else:
                            login = Student.login(email, password)
                            if login == True:
                                print(f"{textColors.green}\tStudent {findStudent} logged in{textColors.reset}")
                                self.showStudentCourseMenu(findStudent, email, password)
                                break
                                
                            
                    
            elif choice == 'r':
                # student registration
                print(f"{textColors.green}\tStudent Sign Up{textColors.reset}")
                while True:
                    email = input("\tEmail: ")
                    password = input("\tPassword: ")
                    if not (Student.getInputEmail(email) and Student.getInputPassword(password)):
                        print(f"{textColors.red}\tIncorrect email or password format{textColors.reset}")
                        continue
                    elif Student.getInputEmail(email) and Student.getInputPassword(password):
                        print(f"{textColors.yellow}\temail and password formats acceptable{textColors.reset}")
                        findStudent = Student.findStudentByEmail(email)
                        if findStudent is not None:
                            print(f"{textColors.red}\tStudent {findStudent} already exists{textColors.reset}")
                            break  
                        else:
                            name = input("\tName: ")
                            name = Student.getInputName(name)
                            Student.registerStudent(name, email, password)
                            print(f"{textColors.green}\tEnrolling Student {name}{textColors.reset}")
                            break
                            # except:
                            #     print(f"{textColors.red}\tFailed to enroll student {name}{textColors.reset}")
                            #     break
                            
                    
            elif choice == 'x':
                break
            else:
                print(f"{textColors.yellow}Invalid choice. Please try again.{textColors.reset}")

    def showStudentCourseMenu(self, name, email, password):
        currentStudent = Student(name, email, password)
        subjectView = subjectController()
        while True:
            choice = input(f"{textColors.cyan}\t\tStudent Course Menu (c/e/r/s/x): {textColors.reset}")
            if choice == 'c':
                # change password
                print(f"{textColors.yellow}\t\tUpdating Password{textColors.reset}")
                while True:
                    new_password = input("\t\tNew Password: ")
                    confirm_new_password = input("\t\tConfirm New Password: ")
                    if new_password == confirm_new_password:
                        currentStudent.changePassword(new_password)
                        print(f"{textColors.yellow}\t\tUpdating Password{textColors.reset}")
                        break
                    else:
                        print(f"{textColors.red}\t\tPasswords does not match - try again{textColors.reset}")
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
    