N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

cnt = 1;
max_cnt = 0;
prev = arr[0]

for i in (arr[1::]) :
    
    
    if (i < 0) == (prev < 0) :
        cnt+=1
        if cnt > max_cnt :
            max_cnt = cnt
    else :
        cnt = 1

    prev = i

print(max_cnt)