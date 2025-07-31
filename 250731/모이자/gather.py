import sys

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

MIN = sys.maxsize

for i in range(n) :
    cnt = 0
    for j in range(n) :
        if i == j :
            continue
        
        d = abs(i - j) 

        cnt += (A[j] * d)

    if cnt < MIN :
        MIN = cnt

print(MIN)