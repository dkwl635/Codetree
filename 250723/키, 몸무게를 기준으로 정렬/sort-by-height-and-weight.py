class Student :
    def __init__ (self,name,height,weight) :
        self.name = name
        self.height = height
        self.weight = weight


n = int(input())

Students = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    student = Student(n_i, int(h_i), int(w_i))
    Students.append(student)

Students.sort(key=lambda x : (x.height ,-x.weight))

for i in Students :
    print(i.name , i.height, i.weight)

# Please write your code here.