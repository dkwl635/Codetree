N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

dirX , dirY= [1,0,-1,0] , [0,1,0,-1]
dir_num = {'E' : 0 , 'N' : 1 , 'W' : 2 , 'S' : 3}


X,Y = 0,0
nX , nY = 0 ,0 
cnt = 0
goal = False
for i in range(N) :
    n_dir = dir[i]
    n_dist = dist[i]
    for _ in range(n_dist) :
        cnt += 1
        dir_n = dir_num[n_dir]
        nX = nX + dirX[dir_n]
        nY = nY + dirY[dir_n]
        if nX == X and nY == Y :
            goal = True
            break
    
    if goal :
        break

if not goal :
    print(-1)
else :
    print(cnt)
