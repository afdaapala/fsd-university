# Assessment 2 – Part 2: Software Development
- Our due date: 9th May 2024
- due date: 20th May 2024

### University system

- [ ]  Go to student menu
- [ ]  Go to the admin menu
- [ ]  exit

### Student system

- [ ]  login
    - [ ]  checked if they exist - only registered student should login
    - [ ]  read student data from “student.data”
    - [ ]  after login, student goes to student course menu
- [ ]  register
    - [ ]  check email and password validation
    - [ ]  checked if they exist
    - [ ]  save student data in “student.data”
- [ ]  exit

### Student Course System

- [ ]  create a system menu
    - [ ]  change
    - [ ]  enrol
    - [ ]  remove
    - [ ]  show
    - [ ]  exit

### Admin System

> Admins already exist in the system. They do not need to login into the system. Admins can simply use the admin sub-system.
- [ ]  clear database file “student.data”
- [ ]  group students: shows the students organized with respect to the grade
- [ ]  partition students: : shows the pass/fail distribution
- [ ]  remove student: remove a student by ID
- [ ]  show: show the students from the data file
- [ ]  exit

## Classes
> The program model has at least the following classes: Student, Subject, and Database. These
classes are responsible for storing the program data and for supplying the program controllers with
functionalities and data. You may add more classes based on Part 1 design.
- [ ]  student
  -  The Student class has the fields:
      - [ ] ID randomly generated 1 <= ID <= 999999, unique and formatted as 6-digits width.
      - [ ] IDs less than 6-digits width should be completed with zeroes from the left.
  - [ ] A student can only enrol in 4 subject maximum
  - [ ] A student can enrol/drop a subject at any time
  - [ ] Upon enrolment in a subject a random mark is generated for this subject 25<= mark <= 100
  - [ ] Upon enrolment in a subject, the grade of that subject is calculated based on the mark
  - [ ] A student pass/fail a course if the average mark of the subjects is greater or equal to 50
  - [ ] A student can change their password at any time.
- [ ]  subject
  - The Subject class has the fields:
  - [ ] ID randomly generated 1 <= ID <= 999, unique and formatted as 3-digits width
  - [ ] IDs less than 3-digits width should be completed with zeroes from the left
  - [ ] mark is randomly generated where 25<= mark <= 100
  - [ ] grade is determined based on the mark
- [ ]  database
  - [ ]  check if the file "students.data" exists before using it
  - [ ]  create the file "students.data" if it doesn’t exists
  - [ ]  write objects to the file "students.data"
  - [ ]  read objects from the file "students.data"
  - [ ]  clear the objects from the file “students.data”
