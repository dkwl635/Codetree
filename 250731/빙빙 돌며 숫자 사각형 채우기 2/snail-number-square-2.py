n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]


# Please write your code here.
def in_range(x,y) :
    return x >= 0 and x < m and y >= 0 and y < n

dir_x,dir_y =[0,1,0,-1],[1,0,-1,0]

cnt = n * m 
dir_cur = 0
x,y = 0,0
arr[0][0] = 1
for i in range(2, cnt + 1) :
    nx,ny = x + dir_x[dir_cur] , y + dir_y[dir_cur];
    if not (in_range(nx, ny) and arr[ny][nx] == 0) :
        dir_cur = (dir_cur + 1) % 4

    x,y = x + dir_x[dir_cur] , y + dir_y[dir_cur];
    
    arr[y][x] = i;

for dy in range(n):
    for dx in range(m):
        print(arr[dy][dx], end = ' ')
    print()

