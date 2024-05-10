import pickle
import os

class Database:
    
    filename = 'Storage/students.data'

    @staticmethod
    def initialize():
        try:
            students = []
            if not os.path.exists(Database.filename):
                with open(Database.filename, 'wb') as file:
                    pickle.dump(students, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')
                   
    @staticmethod
    def read():
        try:
            with open(Database.filename, 'rb') as file:
                students = pickle.load(file)
            return students
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
            return []
        except IOError as e:
            print(f'Reading Error: {e}')
            return []
        
    @staticmethod
    def write(students):
        try:
            with open(Database.filename, 'wb') as file:
                pickle.dump(students, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')

    @staticmethod
    def clear():
        try:
            students = []
            with open(Database.filename, 'wb') as file:
                pickle.dump(students, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')