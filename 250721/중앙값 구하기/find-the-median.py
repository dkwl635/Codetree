A,B,C = map(int, input().split())


if A >= B >= C or C >= B >= A :
    print(B)
elif B >= C >= A or A >= C >= B :
    print(C)
else :
    print(A)