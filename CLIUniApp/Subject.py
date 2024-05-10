import random
from Controller.SubjectController import SubjectController as controller

class Subject:
    def __init__(self, id, mark, grade):
        self.id = id
        self.mark = mark
        self.grade = grade


    @staticmethod
    def generateSubject():
        mark = Subject.generateMark()
        return Subject(Subject.generateId(), mark, Subject.calculateGradeByMark(mark))    
    
    @staticmethod
    def isExistingId(id):
        for student in controller.read():
            for subject in student['subjects']:
                if subject['id'] == id:
                    return True
        return False

    @staticmethod
    def generateId():
        # Generate a random number between 1 and 999
        newSubjectId = str(random.randint(1, 999)).rjust(3, '0')
        if Subject.isExistingId(newSubjectId):
            return Subject.generateId()
        return newSubjectId

    @staticmethod
    def generateMark():
        # Generate a random mark between 25 and 100
        return random.randint(25, 100)

    @staticmethod
    def calculateGradeByMark(mark):
        # Calculate the grade based on the mark generated
        if mark >= 85:
            return 'HD'
        elif mark >= 75 and mark < 85:
            return 'D'
        elif mark >= 65 and mark < 75:
            return 'C'
        elif mark >= 50 and mark < 65:
            return 'P'
        elif mark < 50:
            return 'Z'
