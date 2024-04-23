import random

class Subjects:
    def __init__(self, subjectID=None, mark=None, grade=None):
        self.subjectID = subjectID if subjectID is not None else self.generateSubjectId()
        self.mark = mark if mark is not None else self.generateSubjectMark()
        self.grade = grade if grade is not None else self.calculateGradeByMark()
        self.category = 'PASS' if self.grade != 'F' else 'FAIL'

    def generateSubjectId(self):
        # Generate a random number between 000 and 999
        return f"{random.randint(0, 999):03}"

    def generateSubjectMark(self):
        # Generate a random mark between 0 and 100
        return random.randint(0, 100)

    def calculateGradeByMark(self):
        # Calculate the grade based on the mark generated
        if self.mark >= 90:
            return 'A'
        elif self.mark >= 80:
            return 'B'
        elif self.mark >= 70:
            return 'C'
        elif self.mark >= 60:
            return 'D'
        elif self.mark >= 50:
            return 'E'
        else:
            return 'F'

# Example usage:
subject = Subjects()
print(f"Subject ID: {subject.subjectID}, Mark: {subject.mark}, Grade: {subject.grade}, Category: {subject.category}")
