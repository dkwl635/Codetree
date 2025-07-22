N = int(input())

if N < 2 :
    print("C")


else:
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print("C")
            break;
    else:
        print("P")