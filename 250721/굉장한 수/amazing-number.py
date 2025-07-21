N = int(input())

if (N & 1 and N % 3 == 0) or (N & 0 and N % 5 == 0) :
    print("true")
else:
    print("false")
