n = int(input())
name = []
korean = []
english = []
math = []

class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

students = []
for _ in range(n):
    student_info = input().split()
    student_i = Student(student_info[0],int(student_info[1]),int(student_info[2]),int(student_info[3]))
    students.append(student_i)


students.sort(key=lambda x: (-x.kor,-x.eng,-x.math))

for student in students :
    print(student.name, student.kor, student.eng, student.math, sep=(" "))
