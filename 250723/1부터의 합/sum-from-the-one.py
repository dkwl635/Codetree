N = int(input())

x = 0
for i in range(1,101) :
    x += i
    if x >= N :
        print(i)
        break