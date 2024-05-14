from Styles.Style import textColors
import textwrap

class Admin:
    def __init__(self):
        pass
    
    def viewStudents(self, students):
        # view all students from the database Storage/students.data
        print(f"{textColors.YELLOW}\tStudent List{textColors.DEFAULT}")
        if students.__len__() > 0:
            for student in students:
                print(student)
        else:
            emptyData = '\t\t< Nothing to Display >'
            print(textColors.DEFAULT +  emptyData + textColors.DEFAULT)
        

    def viewStudentsbyGrade(self, students):
        # view students by grade
        listOfGrade = ['Z','P','C','D','HD']
        print(textColors.YELLOW + "\tGrade Grouping" + textColors.DEFAULT)
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
                    print(textColors.DEFAULT +  string + textColors.DEFAULT)
        else:
            emptyData = '\t\t< Nothing to Display >'
            print(textColors.DEFAULT +  emptyData + textColors.DEFAULT)

    def viewStudentsbyCategories(self, students):
        print(textColors.YELLOW + "\tPASS/FAIL Partition" + textColors.DEFAULT)
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
        print(textColors.DEFAULT +  string + textColors.DEFAULT)

        str = f'\tPASS --> [{partPass}]'
        wrapper = textwrap.TextWrapper(subsequent_indent='\t\t  ',width=115) 
        string = wrapper.fill(text=str)
        print(textColors.DEFAULT +  string + textColors.DEFAULT)

    def removeStudent(self, students) -> bool:
        remStudentId = input(textColors.DEFAULT + "\tRemove by ID: " + textColors.DEFAULT)
        remStudent = self.findStudentById(remStudentId, students)
        if remStudent is not None:
            students.remove(remStudent)
            print(textColors.YELLOW + f'\tRemoving Student {remStudentId} Account' + textColors.DEFAULT)
            return True
        else:
            print(textColors.RED + f'\tStudent {remStudentId} does not exist' + textColors.DEFAULT)
            return False

    def removeAllStudents(self, students):
        print(textColors.YELLOW + "\tClearing students database" + textColors.DEFAULT)
        while(1==1):
            subchoice = input(textColors.RED + "\tAre you sure you want to clear the database (Y)ES/(N)O: " + textColors.DEFAULT)  
            if subchoice == 'Y':
                students.clear()
                print(textColors.YELLOW + "\tStudents data cleared" + textColors.DEFAULT)
                return True
            elif subchoice == 'N':
                return False

    def findStudentById(self, id, students):
        for s in students:
            if s.match(id):
                return s
        return None