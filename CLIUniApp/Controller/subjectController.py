from Database import Database

class SubjectController:
    @staticmethod
    def read():
        return Database.read()
    
    @staticmethod
    def enrollSubject(id, subject):
        students = SubjectController.read()
        for student in students:
          if student['id'] == id:
            student['subjects'].append({
              "id": subject.id,
              "mark": subject.mark,
              "grade": subject.grade
            })
            break
        Database.write(students)
        
    @staticmethod
    def removeSubject(id, removeSubject):
        students = SubjectController.read()
        for student in students:
          if student['id'] == id:
            for subject in student['subjects']:
              if subject['id'] == removeSubject.id:
                student['subjects'].remove(subject)
                break
            break
        Database.write(students)
  
