from student import Student
import random
import uuid

def creatingStudents():
    students =[]
    for student in range(10):
        student=Student(str(uuid.uuid4()),random.uniform(1,200),random.uniform(1,10))
        students.append(student)
    return students

for student in creatingStudents():
    print(student.__dict__['marks'])
    print(student.__dict__)
    print(student)