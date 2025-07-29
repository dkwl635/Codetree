n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
# Please write your code here.


dir_x = [0,1,0,-1]
dir_y = [1,0,-1,0]

dir_num = 0

def in_range(x,y) :
    return (x >= 0 and x < n)and (y >= 0 and y < n)

x , y = c - 1 , r - 1

if d == 'D' : dir_num = 2
elif d == 'U' : dir_num = 0
elif d == "R" : dir_num = 1
else : dir_num = 3


for _ in range(t) :
    nx = x + dir_x[dir_num]
    ny = y + dir_y[dir_num]
   
    if in_range(nx,ny) :
        x = nx
        y = ny
    else :
        dir_num = (dir_num + 2) % 4
    
   


print(y+1 , x+1)
        
   
