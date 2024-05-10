#this is for diplaying the subject list
from Styles.Style import textColors
from Models.Subjects import Subjects

class subjectController:
    def showEnrolledSubjectList(self,currentStudent):
        # Show subject list
        subjects = Subjects()
        enrolledSubjects, countEnroll = subjects.showEnrolledSubjects(currentStudent)
        # print(currentStudent.name)
        print(f"{textColors.yellow}\t\tShowing {countEnroll} subjects{textColors.reset}")
        if countEnroll > 0:
            for subject in enrolledSubjects:
                print(f"\t\t[ Subject::{subject['subject_id']} -- mark = {subject['mark']} -- grade = {subject['grade']} ]")
        return None
    
    def enrolSubject(self, currentStudent):
        # Enrol subject
        subjects = Subjects()
        enrol = subjects.EnrolNewSubject(currentStudent)
        if enrol is not None:
            print(f"{textColors.yellow}\t\tEnrolled in {enrol}{textColors.reset}")
        else:
            print(f"{textColors.red}\t\tStudents are allowed to enrol in 4 subjects only{textColors.reset}")
    
    def removeSubject(self, currentStudent):
        # Remove subject
        subjects = Subjects()
        enrolledSubjects, countEnroll = subjects.showEnrolledSubjects(currentStudent)
        print(f"{textColors.yellow}\t\tShowing {countEnroll} subjects{textColors.reset}")
        if countEnroll > 0:
            for subject in enrolledSubjects:
                print(f"\t\t[ Subject::{subject['subject_id']}]")
            subject_id = input(f"{textColors.cyan}\t\tRemove Subject by ID: {textColors.reset}")
            if subjects.removeEnrolledSubject(currentStudent, subject_id):
                print(f"{textColors.yellow}\t\tDropping Subject-{subject_id}{textColors.reset}")
                print(f"{textColors.yellow}\t\tYou are now enrolled in {countEnroll - 1} out of 4 subjects{textColors.reset}")
            else:
                print(f"{textColors.red}\t\tSubject with ID:{subject_id} not found{textColors.reset}")
        else:
            print(f"{textColors.red}\t\tNo subjects found{textColors.reset}")