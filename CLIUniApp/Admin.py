from Color import Color
import textwrap 

class Admin:
    def __init__(self):
        pass

    # View all registered student
    def viewStudents(self, students):
        print(Color.YELLOW + "\tStudent List" + Color.DEFAULT)
        if students.__len__() > 0:
            for student in students:
                print(student)
        else:
            emptyData = '\t\t< Nothing to Display >'
            print(Color.DEFAULT +  emptyData + Color.DEFAULT)

    # Group students by grade
    def viewStudentsbyGrade(self, students):
        listOfGrade = ['Z','P','C','D','HD']
        print(Color.YELLOW + "\tGrade Grouping" + Color.DEFAULT)
        if students.__len__() > 0:
            for grade in listOfGrade:
                studentInGrade = ''
                for student in students:
                    if student.calculateGrade() == grade:
                        if studentInGrade != '':
                            studentInGrade += ', ' + student.studentGrade()
                        else:
                            studentInGrade += student.studentGrade()
                if studentInGrade != '':
                    str = (f'\t{grade.ljust(2)} --> [{studentInGrade}]')
                    wrapper = textwrap.TextWrapper(subsequent_indent='\t\t',width=115) 
                    string = wrapper.fill(text=str)
                    print(Color.DEFAULT +  string + Color.DEFAULT)
                    # print(Color.DEFAULT + f'\t{grade.ljust(2)} --> [{studentInGrade}]' + Color.DEFAULT)
        else:
            emptyData = '\t\t< Nothing to Display >'
            print(Color.DEFAULT +  emptyData + Color.DEFAULT)

    # Partition students by PASS/FAIL
    def viewStudentsbyCategories(self,students):
        print(Color.YELLOW + "\tPASS/FAIL Partition" + Color.DEFAULT)
        partPass = ''
        partFail = ''
        for student in students:
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
        # print out using indentation
        str = f'\tFAIL --> [{partFail}]'
        wrapper = textwrap.TextWrapper(subsequent_indent='\t\t  ',width=115) 
        string = wrapper.fill(text=str)
        print(Color.DEFAULT +  string + Color.DEFAULT)

        str = f'\tPASS --> [{partPass}]'
        wrapper = textwrap.TextWrapper(subsequent_indent='\t\t  ',width=115) 
        string = wrapper.fill(text=str)
        print(Color.DEFAULT +  string + Color.DEFAULT)
        
        # print out standard indentation
        # print(Color.DEFAULT + f'\tFAIL --> [{partFail}]' + Color.DEFAULT)
        # print(Color.DEFAULT + f'\tPASS --> [{partPass}]' + Color.DEFAULT)

    # Remove student
    def removeStudent(self, students) -> bool:
        remStudentId = input(Color.DEFAULT + "\tRemove by ID: " + Color.DEFAULT)
        remStudent = self.findStudentById(remStudentId, students)
        if remStudent is not None:
            students.remove(remStudent)
            print(Color.YELLOW + f'\tRemoving Student {remStudentId} Account' + Color.DEFAULT)
            return True
        else:
            print(Color.RED + f'\tStudent {remStudentId} does not exist' + Color.DEFAULT)
            return False

    # Remove all registered students
    def removeAllStudents(self, students) -> bool:
        print(Color.YELLOW + "\tClearing students database" + Color.DEFAULT)
        while(1==1):
            subchoice = input(Color.RED + "\tAre you sure you want to clear the database (Y)ES/(N)O: " + Color.DEFAULT)  
            if subchoice == 'Y':
                students.clear()
                print(Color.YELLOW + "\tStudents data cleared" + Color.DEFAULT)
                return True
            elif subchoice == 'N':
                return False

    def findStudentById(self, id, students):
        for s in students:
            if s.match(id):
                return s
        return None