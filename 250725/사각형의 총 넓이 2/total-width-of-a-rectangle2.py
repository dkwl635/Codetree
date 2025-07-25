n = int(input())
x1, y1, x2, y2 = [], [], [], []

arr = [[0 for _ in range(201)] for _ in range(201)]


total = 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1 = a + 100
    y1 = b + 100
    x2 = c + 100
    y2 = d + 100

    for x in range(x1,x2) :
        for y in range(y1, y2) :
            if arr[x][y] == 0 :
                arr[x][y] = 1
                total += 1

    
print(total)


# Please write your code here.