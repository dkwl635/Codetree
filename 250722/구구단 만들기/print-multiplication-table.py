A,B = map(int, input().split())


for i in range(1,10) :
    line = ""
    for j in range(B, A -1, -1) :
        if j % 2 == 0:
            line += (f"{j} * {i} = {i*j} / ")

    print(line.rstrip(" / ")) 

        