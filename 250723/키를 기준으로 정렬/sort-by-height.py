n = int(input())
name = []
height = []
weight = []


class Student :
    def __init__(self, name, height, weight) :
        self.name = name
        self.height = int(height)
        self.weight = int(weight)

students = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    Student_i = Student(n_i, int(h_i), int(w_i))
    students.append(Student_i)

students.sort(key=lambda x: x.height)
for student in students :
    print(student.name, student.height, student.weight, sep=(" "))

# Please write your code here.



