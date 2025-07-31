X, Y = map(int, input().split())

# Please write your code here.

MAX = 0
for N in range(X,Y+1) :
    total = 0
    while N > 10 : 
        total += N % 10
        N = N//10

    total += N
    if total > MAX :
        MAX = total

print(MAX)
        