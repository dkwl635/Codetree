N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.

total = N**3
cnt = 0
for i in range(1, N + 1) :
    if i >= a - 2 and i <= a +2 :
        continue
    
    for j in range(1, N + 1) :
        if j >= b - 2 and j <= b + 2 :
            continue
       
        for k in range(1,N + 1):
            if k >= c - 2 and k <= c +2  :
                continue
            
            cnt+=1


total -= cnt
print(total)