N = int(input())


for _ in range(N) :
    x,y = map(int, input().split())
    total = 0
    for i in range(x, y + 1) :
        if i % 2 == 0 :
            total +=i
    
    print(total)
        