
A,B = map(int, input().split())

print(A, end=(" "))
while A < B :
    if A & 1 :
        A*=2
    else :
        A+=3
    if A <= B:
        print(A , end=(" "))
