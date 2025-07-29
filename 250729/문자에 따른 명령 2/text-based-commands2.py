dirs = input()

# Please write your code here.

x, y = 0 , 0
dir_num = 0

dir_x = [0,1,0,-1] 
dir_y = [1,0,-1,0]


for c in dirs : 

    if c == 'F' :
        x += dir_x[dir_num]
        y += dir_y[dir_num]

    if c == 'L' :
        dir_num = dir_num - 1 + 4
    elif c == 'R' :
        dir_num = dir_num + 1
    dir_num %= 4
    


print(x,y)
