
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

MAX = 0
for i in range(n - 2) :
    total = arr[i] + arr[i+1] + arr[i+2]
    
    if total > MAX :
        MAX = total

print(MAX)
    
