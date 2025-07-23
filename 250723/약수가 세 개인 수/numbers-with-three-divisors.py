start, end = map(int, input().split())

# Please write your code here.

total = 0
for x in range(start , end+1) :
    cnt = 0
    for i in range(1, x +1) :
        if x % i == 0 :
            cnt+=1
    
    if cnt == 3 :
        total+=1

print(total)
