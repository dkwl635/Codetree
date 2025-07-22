N = int(input())

arr = []
x = list(map(int, input().split()))
x.reverse()

for i in (x) : 
    if i % 2 == 0 :
        arr.append(i)
   
print(*arr , sep=" ")