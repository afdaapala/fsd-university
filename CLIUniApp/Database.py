import os
import pickle

FILE_NAME = 'students.data'

class Database:
    def __init__(self):
      pass
  
    @staticmethod
    def initialize():
        try:
            students = []
            if not os.path.exists(FILE_NAME):
                with open(FILE_NAME, 'wb') as file:
                    pickle.dump(students, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')

    # Should be substitued with Database function
    @staticmethod
    def read():
        try:
            with open(FILE_NAME, 'rb') as file:
                students = pickle.load(file)
            return students
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
            return []
        except IOError as e:
            print(f'Reading Error: {e}')
            return []

    # Should be substitued with Database function
    @staticmethod
    def write(students):
        try:
            with open(FILE_NAME, 'wb') as file:
                pickle.dump(students, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')
            
Database.initialize()