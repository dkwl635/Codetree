A,B = map(str, input().split())

if len(A) > len(B) :
    print(f"{A} {len(A)}")
elif len(B) > len(A) :
    print(f"{B} {len(B)}")
else :
    print("same")