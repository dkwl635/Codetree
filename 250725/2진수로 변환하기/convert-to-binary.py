n = int(input())

arr = []
while n > 1 :
    arr.append(n%2)
    n //= 2

arr.append(n)
print(*arr[::-1],sep=(""))
# Please write your code here.