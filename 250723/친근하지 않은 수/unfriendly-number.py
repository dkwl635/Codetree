N = int(input())

num = 0

for i in range(1, N+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 :
       continue
    num+=1
    

print(num)