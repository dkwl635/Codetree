arr =[ list(map(int, input().split())), list(map(int, input().split())) , list(map(int, input().split()))]


for i in range(len(arr)) :
    for j in range(len(arr[i])) :
        arr[i][j]*=3
        print(arr[i][j], end=" ")
    print()

