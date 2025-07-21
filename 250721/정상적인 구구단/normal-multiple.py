N = int(input())
N+=1

for i in range(1, N) :
    for j in range(1, N) :
        print(f"{i} * {j} = {i * j}" , end=(""))
        if j == N -1 :
            print("")
        else :
            print(", ", end="")
           