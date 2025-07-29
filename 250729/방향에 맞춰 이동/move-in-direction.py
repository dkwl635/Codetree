n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x = y = 0
dir_xy = [{1,0} ,{}]
for d, s in (moves) :
    s = int(s)
    if d == 'W' :
        x -= s
    elif d == 'E' :
        x += s
    elif d == 'N' :
        y += s
    else :
        y -= s

print(x,y)
