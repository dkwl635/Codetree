N = int(input())

for i in range(1, N + 1) : 
    for j in range(i) :
        print(i, end =" ")
        if j == i -1 :
            print()
