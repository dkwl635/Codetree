n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

def in_range(x,y) :
    return (x >= 0 and x < n)and (y >= 0 and y < n)

# Please write your code here.
dirX , dirY= [1,0,-1,0] , [0,1,0,-1]

grid = [[0 for _ in range(n)] for _ in range(n)]



for y , x in (points) :
    grid[y - 1][x- 1] = 1
    cnt_1 = 0
    for i in range(4) :
        nx = x-1 + dirX[i]
        ny = y-1 + dirY[i]
        if in_range(nx, ny) and grid[ny][nx] :
            cnt_1 +=1 

    if cnt_1 == 3 :
        print(1)
    else :
        print(0)


