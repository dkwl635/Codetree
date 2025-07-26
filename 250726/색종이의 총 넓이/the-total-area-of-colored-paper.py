n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
# Please write your code here.

arr = [[0 for _ in range(201)] for _ in range(201)]
cnt = 0
for p1, p2 in(points) :
    for x in range(p1, p1+8) :
        for y in range(p2, p2 + 8) :
            if arr[x][y] == 0 :
                arr[x][y] = 1
                cnt+=1

print(cnt)