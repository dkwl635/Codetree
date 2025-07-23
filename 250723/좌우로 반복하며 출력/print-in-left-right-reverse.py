N = int(input())

arr = [[ 0 for _ in range(N)] for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        arr[i][j] = j+1
    
    if i % 2 != 0 :
        arr[i].reverse()
    print(*arr[i], sep="")

