#this is for diplaying the subject list
from Styles.Style import textColors
from Models.Subjects import Subjects

class subjectController:
    def showEnrolledSubjectList(self,currentStudent):
        # Show subject list
        subjects = Subjects()
        enrolledSubjects, countEnroll = subjects.showEnrolledSubjects(currentStudent)
        # print(currentStudent.name)
        print(f"{textColors.YELLOW}\t\tShowing {countEnroll} subjects{textColors.DEFAULT}")
        if countEnroll > 0:
            for subject in enrolledSubjects:
                print(f"\t\t[ Subject::{subject['subject_id']} -- mark = {subject['mark']} -- grade = {subject['grade']} ]")
        return None
    
    def enrolSubject(self, currentStudent):
        # Enrol subject
        subjects = Subjects()
        enrol = subjects.EnrolNewSubject(currentStudent)
        if enrol is not None:
            print(f"{textColors.YELLOW}\t\tEnrolled in {enrol}{textColors.DEFAULT}")
        else:
            print(f"{textColors.RED}\t\tStudents are allowed to enrol in 4 subjects only{textColors.DEFAULT}")
    
    def removeSubject(self, currentStudent):
        # Remove subject
        subjects = Subjects()
        enrolledSubjects, countEnroll = subjects.showEnrolledSubjects(currentStudent)
        print(f"{textColors.YELLOW}\t\tShowing {countEnroll} subjects{textColors.DEFAULT}")
        if countEnroll > 0:
            for subject in enrolledSubjects:
                print(f"\t\t[ Subject::{subject['subject_id']}]")
            subject_id = input(f"{textColors.CYAN}\t\tRemove Subject by ID: {textColors.DEFAULT}")
            if subjects.removeEnrolledSubject(currentStudent, subject_id):
                print(f"{textColors.YELLOW}\t\tDropping Subject-{subject_id}{textColors.DEFAULT}")
                print(f"{textColors.YELLOW}\t\tYou are now enrolled in {countEnroll - 1} out of 4 subjects{textColors.DEFAULT}")
            else:
                print(f"{textColors.RED}\t\tSubject with ID:{subject_id} not found{textColors.DEFAULT}")
        else:
            print(f"{textColors.RED}\t\tNo subjects found{textColors.DEFAULT}")