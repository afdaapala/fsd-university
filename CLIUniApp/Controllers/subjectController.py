#this is for diplaying the subject list
from Models.Database import Database

class subjectController:
    @staticmethod
    def enrollSubject(id, subject):
        students = Database.read()
        for student in students:
          if student.id == id:
            student.subjects.append(subject)
            break
        Database.write(students)

    @staticmethod
    def removeSubject(id, removeSubject):
        students = Database.read()
        for student in students:
          if student.id == id:
            for subject in student.subjects:
              if subject.id == removeSubject.id:
                student.subjects.remove(subject)
                break
            break
        Database.write(students)