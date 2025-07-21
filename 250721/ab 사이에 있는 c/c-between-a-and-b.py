a ,b, c = map(int, input().split())

x = "NO"
for i in range(a , b+ 1) :
    if i % c == 0 :
        x = "YES"

print(x)