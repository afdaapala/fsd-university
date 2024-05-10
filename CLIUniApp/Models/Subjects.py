import random
from Models.Database import Database

class Subjects:

    def generateSubjectId(self):
        # Generate a random number between 000 and 999
        return f"{random.randint(0, 999):03}"

    def generateSubjectMark(self):
        # Generate a random mark between 0 and 100
        return random.randint(30, 100)

    def calculateGradeByMark(self, mark):
        # Calculate grade based on the mark
        if mark < 50:
            return 'F'
        elif mark < 65:
            return 'P'
        elif mark < 75:
            return 'C'
        elif mark < 85:
            return 'D'
        else:
            return 'HD'
        
    def EnrolNewSubject(self, currentStudent):
        # Enrol new subject
        database = Database()
        student = database.loadLoginStudent(currentStudent)
        countenrol = len(student['subjects'])
        # print(student['name'])
        # print(student['subjects'])
        # print(countenrol)
        
        #calculate currentUser Enrolled subjects
        
        if countenrol < 4:
            subject_Id = self.generateSubjectId()
            subject_name = 'Subject-' + subject_Id
            subject_mark = self.generateSubjectMark()
            subject_grade = self.calculateGradeByMark(subject_mark)
            new_subject = {
                "subject_name": subject_name,
                "subject_id": subject_Id,
                "mark": subject_mark,
                "grade": subject_grade
            }
            student['subjects'].append(new_subject)
            # print(student['subjects'])
            # print(student)
            database.saveLoginStudent(student)
            return subject_name
        else:
            return None
        
    def removeEnrolledSubject(self, currentStudent, subject_id):
        # Remove enrolled subject
        database = Database()
        student = database.loadLoginStudent(currentStudent)
        enrolledSubjects = student['subjects']
        for subject in enrolledSubjects:
            if subject['subject_id'] == subject_id:
                enrolledSubjects.remove(subject)
                student['subjects'] = enrolledSubjects
                database.saveLoginStudent(student)
                return True
        return False
        
    def showEnrolledSubjects(self, currentStudent):
        # Show enrolled subjects
        database = Database()
        student = database.loadLoginStudent(currentStudent)
        enrolledSubjects = student['subjects']
        if enrolledSubjects is None:
            Enrolcount = 0
        else:
            Enrolcount = len(student['subjects'])
            # enroled = student['subjects']
            # for subject in student['subjects']:
            #     enrolledSubjects.append(f"{subject['subject_name']} - {subject['subject_id']} - {subject['grade']}")
        return enrolledSubjects, Enrolcount

# Example usage:
# subject = Subjects()
# print(f"Subject ID: {subject.subjectID}, Mark: {subject.mark}, Grade: {subject.grade}, Category: {subject.category}")
