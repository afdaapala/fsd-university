from Color import Color
from Database import Database

#for dummy
import random
from Subjects import Subjects

class AdminController:
    def __init__(self, students) -> None:
        self.students = students
        self.listOfGrade = ['Z','P','C','D','HD']

    def showAdminMenu(self):
        # Show admin menu
        while True:
            choice = input(Color.CYAN + "\tAdmin system (c/g/p/r/s/x): " + Color.DEFAULT)    
            if choice == 'c':
                # clear database file
                print(Color.YELLOW + "\tClearing students database" + Color.DEFAULT)
                while(1==1):
                    subchoice = input(Color.RED + "\tAre you sure you want to clear the database (Y)ES/(N)O: " + Color.DEFAULT)  
                    if subchoice == 'Y':
                        Database.clear()
                        self.students.clear()
                        print(Color.YELLOW + "\tStudents data cleared" + Color.DEFAULT)
                        break
                    elif subchoice == 'N':
                        break
    
            elif choice == 'g':
                # group students
                print(Color.YELLOW + "\tGrade Grouping" + Color.DEFAULT)
                if self.students.__len__() > 0:
                    for grade in self.listOfGrade:
                        studentInGrade = ''
                        for student in self.students:
                            if student.calculateGrade() == grade:
                                if studentInGrade != '':
                                    studentInGrade += ', ' + student.studentGrade()
                                else:
                                    studentInGrade += student.studentGrade()
                        if studentInGrade is not '':
                            print(f'\t{grade.ljust(2)} --> [{studentInGrade}]')
                else:
                    emptyData = '\t\t< Nothing to Display >'
                    print(Color.DEFAULT +  emptyData + Color.DEFAULT)

            elif choice == 'p':
                # partition students
                print(Color.YELLOW + "\tPASS/FAIL Partition" + Color.DEFAULT)
                partPass = ''
                partFail = ''
                for student in self.students:
                    if student.calculateGrade() == 'Z':
                        if partFail != '':
                            partFail += ', ' + student.studentGrade()
                        else:
                            partFail += student.studentGrade()
                    else:
                        if partPass != '':
                            partPass += ', ' + student.studentGrade()
                        else:
                            partPass += student.studentGrade()
                # print out
                print(Color.DEFAULT + f'\tFAIL --> [{partFail}]' + Color.DEFAULT)
                print(Color.DEFAULT + f'\tPASS --> [{partPass}]' + Color.DEFAULT)

            elif choice == 'r':
                # remove student
                remStudentId = input(Color.DEFAULT + "\tRemove by ID: " + Color.DEFAULT)
                remStudent = self.findStudentById(remStudentId)
                if remStudent is not None:
                    self.students.remove(remStudent)
                    Database.write(self.students)
                    print(Color.YELLOW + f'\tRemoving Student {remStudentId} Account' + Color.DEFAULT)
                else:
                    print(Color.RED + f'\tStudent {remStudentId} does not exist' + Color.DEFAULT)


            elif choice == 's':
                # show student
                print(Color.YELLOW + "\tStudent List" + Color.DEFAULT)
                if self.students.__len__() > 0:
                    for student in self.students:
                        print(student)
                else:
                    emptyData = '\t\t< Nothing to Display >'
                    print(Color.DEFAULT +  emptyData + Color.DEFAULT)

            elif choice == 'x':
                break

            #dummy purpose
            elif choice == 'd':
                for a in range(0,5):
                    self.students.append(StudentDummy())
                Database.write(self.students)
            else:
                print("\tInvalid choice. Please try again.")
    
    def findStudentById(self, id):
        for s in self.students:
            if s.match(id):
                return s
        return None


class StudentDummy:
    def __init__(self) -> None:
        randStr = f"{random.randint(0, 999):03}"
        self.studentid = randStr
        self.name = 'Student ' + randStr
        self.email = self.name + '@university.com'
        self.password = 'pass'
        self.subjects = []
        for a in range(0,4):
            self.subjects.append(Subjects())

    def __str__(self) -> str:
        return Color.DEFAULT + f'\t{self.name} :: {self.studentid} --> Email: {self.email}' + Color.DEFAULT
    
    def studentGrade(self) -> str:
        return f'{self.name} :: {self.studentid} --> GRADE: {self.calculateGrade()} - MARK: {self.calculateMark():.2f}'
    
    def calculateGrade(self) -> str:
        grade = '-'
        averageMark = self.calculateMark()
        if averageMark < 50:
            grade = 'Z'
        elif averageMark >= 50 and averageMark < 65:
            grade = 'P'
        elif averageMark >= 65 and averageMark < 75:
            grade = 'C'
        elif averageMark >= 75 and averageMark < 85:
            grade = 'D'
        elif averageMark >= 85:
            grade = 'HD'
        return grade

    def calculateMark(self) -> int:
        total = 0
        average = 0
        if self.subjects != None and self.subjects.__len__() > 0:
            for subject in self.subjects:
                total += subject.mark
            average = total / self.subjects.__len__()
        return average
    
    def match(self, studentId):
        return self.studentid == studentId