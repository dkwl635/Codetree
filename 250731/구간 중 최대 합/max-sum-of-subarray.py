
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

MAX = 0
for i in range(n - k + 1) :
    total = arr[i]
    for j in range(i + 1 , i + k) :
        total += arr[j]

    if total > MAX :
        MAX = total

print(MAX)
    
