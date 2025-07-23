N = 10

cnt_3 , cnt_5 =0,0

for i in range(N) :
    temp = int(input())
    if temp % 3 == 0 :
        cnt_3+=1
    if temp % 5 == 0 :
        cnt_5+=1


print(f"{cnt_3} {cnt_5}")