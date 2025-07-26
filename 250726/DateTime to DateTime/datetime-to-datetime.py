a, b, c = map(int, input().split())
# Please write your code here.


start_day = 11
start_hour = 11
start_min = 11

end_day = a
end_hour = b
end_min = c

total = 0

 

while not (start_day == end_day and start_hour == end_hour and start_min == end_min) :
    total+=1
    start_min +=1
    if(start_min == 60) :
        start_min = 0
        start_hour+=1
    
    if(start_hour == 24) :
        start_hour = 0
        start_day +=1
     
if start_day > end_day and start_hour > end_hour and start_min > end_min :
    print(-1)   
else :
    print(total)