#input value
A,B = map(int, input().split())

#B A,-1 for
for i in range(B, A -1 , -1):
    print(i, end=" ")
