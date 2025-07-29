n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.

cnt = 0

dir_x = [0,1,0,-1]
dir_y = [1,0,-1,0]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n 

for y in range (n) :
    for x in range(n) :
        cnt_1 = 0
        for dx,dy in zip(dir_x, dir_y) :
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny) and grid[ny][nx] == 1 :
                cnt_1 += 1

        if cnt_1 >= 3 :
            cnt += 1


print(cnt)