N = int(input())
x = 1

for i in range(1, N+1) :
    for j in range(i) :
        print(x, end=" ")
        x+=1
    
    print()
