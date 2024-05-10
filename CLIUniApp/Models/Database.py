import pickle
import random
import random

class Database:
    def __init__(self):
      pass
    
    #this is a dummy data for testing purpose dont forget to remove it when merging
    # def dummyData(self):
    #   student1 = {
    #     "name": "John Doe",
    #     "id" : random.randint(100000, 999999),
    #     "email": "john.doe@university.com",
    #     "password": "Helloworld123",
    #     "subjects": []
    #   }
    #   student2 = {
    #     "name": "Jane Doe",
    #     "id" : random.randint(100000, 999999),
    #     "email": "jane.doe@university.com",
    #     "password": "Helloworld123",
    #     "subjects": []
    #   }
    #   student3 = {
    #     "name": "Alice Smith",
    #     "id" : random.randint(100000, 999999),
    #     "email": "alice.smith@university.com",
    #     "password": "Helloworld123",
    #     "subjects": []
    #   }
    #   student4 = {
    #     "name": "Bob Johnson",
    #     "id" : random.randint(100000, 999999),
    #     "email": "bob.johnson@university.com",
    #     "password": "Helloworld123",
    #     "subjects": []
    #   }
    #   student5 = {
    #     "name": "Emily Davis",
    #     "id" : random.randint(100000, 999999),
    #     "email": "emily.davis@university.com",
    #     "password": "Helloworld123",
    #     "subjects": []
    #   }

    #   students = [student1, student2, student3, student4, student5]
      
    #   #insert grade for each student (dummy data  for testing purpose)
    #   for student in students:
    #       student['mark'] = round(random.uniform(0, 100), 2)
    #       if student['mark'] < 50:
    #           student['grade'] = 'F'
    #       elif student['mark'] < 65:
    #           student['grade'] = 'P'
    #       elif student['mark'] < 75:
    #           student['grade'] = 'C'
    #       elif student['mark'] < 85:
    #           student['grade'] = 'D'
    #       else:
    #           student['grade'] = 'HD'
      
          
          
    #   with open('Storage/students.data', 'wb') as file:
    #       pickle.dump(students, file)
    
    def save_student(self, student):
      # Save a student to 'students.data'
      students = self.load_students()
      students.append(student)
      with open('Storage/students.data', 'wb') as file:
          pickle.dump(students, file)
          
    def loadLoginStudent(self, currentStudent):
      # Load a student info from students.data
      students = self.load_students()
      currentEmail = currentStudent.email
      # print(currentEmail)
      studentData = []
      for student in students:
          if student['email'] == currentEmail:
              studentData = student
              # print(student['email'] + " match " + currentEmail)
              # print(studentData)
              break
      return studentData
    
    def saveLoginStudent(self, updatedStudentData):
      # Save a student info to students.data
      students = self.load_students()
      # print("this is student data before insert to students.data file")
      # print(updatedStudentData)
      for student in students:
          if student['email'] == updatedStudentData['email']:
              student.update(updatedStudentData)
              with open('Storage/students.data', 'wb') as file:
                  pickle.dump(students, file)
              break
      
          
    def load_students(self):       
      # Load students from 'students.data'
      try:
          with open('Storage/students.data', 'rb') as file:
              return pickle.load(file)
      except FileNotFoundError:
          print("Error. Data not found")
          print("Creating new data file...")
          with open('Storage/students.data', 'wb') as file:
              pickle.dump([], file)
          print("Data file created.")
          return [] # Return an empty list if the file does not exist
    
    def removeStudent(self, student_id):
      # Remove student by student_id
      students = self.load_students()
      for student in students:
          if student['id'] == student_id:
              students.remove(student)
              with open('Storage/students.data', 'wb') as file:
                  pickle.dump(students, file)
              return True
      return False
    
    def clearAllData(self):
        # Delete all data from 'students.data'
        with open('Storage/students.data', 'wb') as file:
            pickle.dump([], file)

# database = Database()
# database.dummyData()