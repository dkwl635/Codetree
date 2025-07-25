n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
arr = [0 for _ in range(n + 1)]

cnt = 0
for i in range(k) :
    for j in range(commands[i][0] , commands[i][1] + 1) :
        arr[j] +=1
        if(cnt < arr[j]) :
            cnt = arr[j]

print(cnt)