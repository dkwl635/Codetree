N,M = map( int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(4)]
arr2 = [list(map(int, input().split())) for _ in range(4)]


for i in range(4) :
    for j in range(4) :
        if arr1[i][j] == arr2[i][j] :
            print("0", end=" ")
        else :
            print("1", end=" ")
    print()