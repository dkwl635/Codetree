n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.



min_value = 40001**2 
for i in range(n):
    min_X = 40001
    min_Y = 40001
    max_X = 0
    max_Y = 0
    for j in range(n) :
        if i == j : 
            continue 

        min_X = min(min_X, x[j])
        min_Y = min(min_Y, y[j])
        max_X = max(max_X ,x[j])
        max_Y = max(max_Y, y[j])
        
    value = (max_X - min_X) * (max_Y - min_Y)
    if min_value > value :
        min_value = value

print(value)