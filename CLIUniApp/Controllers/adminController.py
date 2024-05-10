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
            choice = input(textColors.cyan + "\tAdmin system (c/g/p/r/s/x): " + textColors.reset)
            if choice == 'c':
                # clear all students from the database
                print(textColors.yellow + "\tClearing students database" + textColors.reset)
                choice = input(textColors.red + "\tAre you sure you want to clear the database? (Y)ES/(N)O: " + textColors.reset)
                if choice.upper() == 'Y':
                    admin.removeAllStudents()
                    print(textColors.red + "\tDatabase cleared" + textColors.reset)
                elif choice.upper() == 'N':
                    print(textColors.yellow + "\tDatabase not cleared" + textColors.reset)
                else:
                    print(textColors.yellow + "\tInvalid choice. Please try again." + textColors.reset)
            elif choice == 'g':
                # group students by grade
                F, P, C, D, HD = admin.viewStudentsbyGrade()
                if F or P or C or D or HD:
                    print(textColors.yellow + "\tGrade Grouping" + textColors.reset)
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
                    print(textColors.yellow + "\tNo students found" + textColors.reset)
                
            elif choice == 'p':
                # partition students by categories
                passGroup, failGroup = admin.viewStudentsbyCategories()
                if passGroup or failGroup:
                    print(textColors.yellow + "\tPASS/FAIL Partition" + textColors.reset)
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
                    print(textColors.yellow + "\tNo students found" + textColors.reset)
                
            elif choice == 'r':
                # Remove student
                while True:
                    student_id = input("\tRemove by ID (press 'x' to cancel): ")
                    if student_id == 'x':
                        break
                    elif student_id.isdigit():
                        student_id = int(student_id)
                        if student_id not in [student['id'] for student in admin.viewStudents()]:
                            print(f"{textColors.red}\tStudent {student_id} does not exist{textColors.reset}")
                        else:
                            try:
                                admin.removeStudent(student_id)
                                print(f"{textColors.yellow}\tRemoving Student {student_id} Account {textColors.reset}")
                            except:
                                print(f"{textColors.red}\tFailed to remove student {student_id}{textColors.reset}")
                        break
                    elif not student_id:
                        print(textColors.yellow + "\tInvalid input. Please try again." + textColors.reset)
                    else:
                        print(textColors.yellow + "\tInvalid input. ID must be a number." + textColors.reset)
                
            elif choice == 's':
                # Student List
                print(textColors.yellow + "\tStudent List" + textColors.reset)
                students = admin.viewStudents()
                if not students:
                    print(textColors.red + "\tNo students found" + textColors.reset)
                else:
                    for student in students:
                        print(f"\t{student['name']} :: {student['id']} --> Email: {student['email']}")
            elif choice == 'x':
                break
            else:
                print(textColors.fail + "\tInvalid choice. Please try again." + textColors.reset)