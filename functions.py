class Student:
    count = 0
    count_of_ce_students = 0
    count_of_cse_students = 0
    count_of_ece_students = 0
    count_of_eee_students = 0
    count_of_me_students = 0
    
    def __init__(self, roll_no, name, branch, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.branch = branch
        self.cgpa = cgpa
        Student.count += 1
        if branch == 'CE' or branch == 'ce'or branch == 'Ce':
            Student.count_of_ce_students += 1
        elif branch == 'CSE' or branch == 'cse' or branch == 'Cse':
            Student.count_of_cse_students += 1
        elif branch == 'ECE' or branch == 'ece' or branch == 'Ece':
            Student.count_of_ece_students += 1
        elif branch == 'EE' or branch == 'ee' or branch == 'Ee':
            Student.count_of_eee_students += 1
        elif branch == 'ME' or branch == 'me' or branch == 'Me':
            Student.count_of_me_students += 1
    def display(self):
        print(f"Roll no: {self.roll_no}, Name: {self.name}, Branch: {self.branch}, CGPA: {self.cgpa}")
with open('students.txt','r') as f:
    students = []
    for line in f:
        roll,name,branch,cgpa = line.strip().split(',')
        if line:
            student = Student(roll,name,branch,cgpa)
            students.append(student)
def add_student():
    roll_no = input('Enter student roll number:')
    for student in students:
        if student.roll_no == roll_no:
            print ('student already exists')
            return
    name = input('Enter student name:')
    branch = input('Enter student branch:')
    cgpa = input('Enter student cgpa:')
    student = Student(roll_no, name, branch, cgpa)
    students.append(student)
    print ('student added successfully')
def view_students():
    for student in students:
        student.display()
    print ('student viewed')
def search_students():
    roll = input('Enter student roll number to search:')
    for student in students:
        if student.roll_no == roll:
            student.display()
            return
    print ('student not found')

def delete_students():
    roll = input('Enter student roll number to delete:')
    for student in students:
        if student.roll_no == roll:
            students.remove(student)
            Student.count -= 1
            print ('student deleted')
            return
    print ('student not found')
def total_students():
    print(f'Total number of students: {Student.count}')
    print(f'Total number of CE students: {Student.count_of_ce_students}')
    print(f'Total number of CSE students: {Student.count_of_cse_students}')
    print(f'Total number of ECE students: {Student.count_of_ece_students}')
    print(f'Total number of EEE students: {Student.count_of_eee_students}')
    print(f'Total number of ME students: {Student.count_of_me_students}')
def update_students():
   roll = input('Enter student roll number to update:')
   for student in students:
       if student.roll_no == roll:
           new_name = input('Enter new name:')
           new_branch = input('Enter new branch:')
           new_cgpa = input('Enter new cgpa:')
           student.name = new_name
           student.branch = new_branch
           student.cgpa = new_cgpa
           print ('student updated')
           return
   print ('student not found')
def find_topper():
    topper = students[0]
    for student in students:
        if student.cgpa > topper.cgpa:
                 topper = student
    
    print(f"Topper : {topper.name}({topper.cgpa})")
def average_cgpa():
    total_cgpa = 0
    for student in students:
        total_cgpa += float(student.cgpa)
    print(f'Average CGPA: {total_cgpa/Student.count}')
def exitsaving():
    with open('students.txt', 'w') as f:
        for student in students:
            f.write(f"{student.roll_no},{student.name},{student.branch},{student.cgpa}\n")
    print ('student data saved successfully')
def sortbyname():
    students.sort(key=lambda s: s.name)
    print("Sorted by name")
def sortbyroll():
    students.sort(key=lambda s: s.roll_no)
    print("Sorted by roll")
def sortbycgpa():
    students.sort(key=lambda s: s.cgpa)
    print("Sorted by cgpa")
def studentreport():
    print(f"""===student report===
Total students : {Student.count}
Branch distribution:
ME :{Student.count_of_me_students}
CSE:{Student.count_of_cse_students}
EE :{Student.count_of_eee_students}
CE :{Student.count_of_ce_students}
ECE:{Student.count_of_ece_students}""")
    average_cgpa()
    find_topper()
