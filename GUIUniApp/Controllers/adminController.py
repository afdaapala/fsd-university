from Styles.Style import textColors
from Models.Admin import Admin

# admin controller to handle user request no need to login
class adminController:
    def __init__(self):
        pass

    def showAdminMenu(self):
        admin = Admin()
        # Show admin menu
        while True:
            choice = input(textColors.CYAN + "\tAdmin system (c/g/p/r/s/x): " + textColors.DEFAULT)
            if choice == 'c':
                # clear all students from the database
                print(textColors.YELLOW + "\tClearing students database" + textColors.DEFAULT)
                choice = input(textColors.RED + "\tAre you sure you want to clear the database? (Y)ES/(N)O: " + textColors.DEFAULT)
                if choice.upper() == 'Y':
                    admin.removeAllStudents()
                    print(textColors.RED + "\tDatabase cleared" + textColors.DEFAULT)
                elif choice.upper() == 'N':
                    print(textColors.YELLOW + "\tDatabase not cleared" + textColors.DEFAULT)
                else:
                    print(textColors.YELLOW + "\tInvalid choice. Please try again." + textColors.DEFAULT)
            elif choice == 'g':
                # group students by grade
                F, P, C, D, HD = admin.viewStudentsbyGrade()
                if F or P or C or D or HD:
                    print(textColors.YELLOW + "\tGrade Grouping" + textColors.DEFAULT)
                    if F:
                        print("\tF -->")
                        for student in F:
                            print(f"\t{student['name']} :: {student['id']} --> GRADE: {student['grade']} - MARK: {student['mark']}")
                    if P:
                        print("\tP -->")
                        for student in P:
                            print(f"\t{student['name']} :: {student['id']} --> GRADE: {student['grade']} - MARK: {student['mark']}")
                    if C:
                        print("\tC -->")
                        for student in C:
                            print(f"\t{student['name']} :: {student['id']} --> GRADE: {student['grade']} - MARK: {student['mark']}")
                    if D:
                        print("\tD -->")
                        for student in D:
                            print(f"\t{student['name']} :: {student['id']} --> GRADE: {student['grade']} - MARK: {student['mark']}")
                    if HD:
                        print("\tHD -->")
                        for student in HD:
                            print(f"\t{student['name']} :: {student['id']} --> GRADE: {student['grade']} - MARK: {student['mark']}")
                else:
                    print(textColors.YELLOW + "\tNo students found" + textColors.DEFAULT)
                
            elif choice == 'p':
                # partition students by categories
                passGroup, failGroup = admin.viewStudentsbyCategories()
                if passGroup or failGroup:
                    print(textColors.YELLOW + "\tPASS/FAIL Partition" + textColors.DEFAULT)
                    if failGroup:
                        print("\tFail -->")
                        for student in failGroup:
                            print(f"\t{student['name']} :: {student['id']} --> GRADE: {student['grade']} - MARK: {student['mark']}")
                    else:
                        print("\tFail --> []")
                    if passGroup:
                        print("\tPass -->")
                        for student in passGroup:
                            print(f"\t{student['name']} :: {student['id']} --> GRADE: {student['grade']} - MARK: {student['mark']}")
                    else:
                        print("\tPass --> []")
                else:
                    print(textColors.YELLOW + "\tNo students found" + textColors.DEFAULT)
                
            elif choice == 'r':
                # Remove student
                while True:
                    student_id = input("\tRemove by ID (press 'x' to cancel): ")
                    if student_id == 'x':
                        break
                    elif student_id.isdigit():
                        student_id = int(student_id)
                        if student_id not in [student['id'] for student in admin.viewStudents()]:
                            print(f"{textColors.RED}\tStudent {student_id} does not exist{textColors.DEFAULT}")
                        else:
                            try:
                                admin.removeStudent(student_id)
                                print(f"{textColors.YELLOW}\tRemoving Student {student_id} Account {textColors.DEFAULT}")
                            except:
                                print(f"{textColors.RED}\tFailed to remove student {student_id}{textColors.DEFAULT}")
                        break
                    elif not student_id:
                        print(textColors.YELLOW + "\tInvalid input. Please try again." + textColors.DEFAULT)
                    else:
                        print(textColors.YELLOW + "\tInvalid input. ID must be a number." + textColors.DEFAULT)
                
            elif choice == 's':
                # Student List
                print(textColors.YELLOW + "\tStudent List" + textColors.DEFAULT)
                students = admin.viewStudents()
                if not students:
                    print(textColors.RED + "\tNo students found" + textColors.DEFAULT)
                else:
                    for student in students:
                        print(f"\t{student['name']} :: {student['id']} --> Email: {student['email']}")
            elif choice == 'x':
                break
            else:
                print(textColors.fail + "\tInvalid choice. Please try again." + textColors.DEFAULT)