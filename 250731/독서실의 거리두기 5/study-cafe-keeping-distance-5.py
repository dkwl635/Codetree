N = int(input())
seat = input()

# Please write your code here.


arr = list(seat)


total = 0
for i in range(N) :
    if arr[i] == '1' : continue
    
    cnt = 0

    cnt_L = 1
    cnt_R = 1

    for L in range(i-1 , -1 , -1) :
        if arr[L] == '1':
            break
        if cnt_L == 0 :
            cnt = 100
        else :
            cnt_L += 1
    
    for R in range(i+1, N) :
        if arr[R] == '1' :
            break  
        else :
            cnt_R += 1

    if i == N - 1 :
        cnt_R = 100
    if i == 0 :
        cnt_L = 100
    
    
    cnt = min(cnt_L , cnt_R)
    
    if total < cnt :
        #print(i , cnt_L , cnt_R)
        total = max(total , cnt)

print(total)

    
    

