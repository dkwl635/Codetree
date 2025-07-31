n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.
MAX = 0
for i in range(1,4) :
    answer = i
    cnt = 0
    for j in range (n) :
       
        if a[j] == answer :
            answer = b[j] 
        elif b[j] == answer :
            answer = a[j]

        if answer == c[j] :
            cnt += 1

    if MAX < cnt :
        MAX = cnt

print(MAX)