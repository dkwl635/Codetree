n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0 for _ in range(101)]

cnt = 0

for segments in (segments) :
    for i in range(segments[0], segments[1] + 1) :
        arr[i]+=1
        if arr[i] > cnt :
            cnt = arr[i]

print(cnt)