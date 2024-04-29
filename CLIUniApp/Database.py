import json
# need to change to pickle

class Database:
    def __init__(self):
      pass
  
    def load_students(self):
      # Load students from 'students.data'
      try:
          with open('students.data', 'r') as file:
              return json.load(file)
      except FileNotFoundError:
          return []  # Return an empty list if the file does not exist