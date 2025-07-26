N = input()

# Please write your code here.

dec = 0
base = 1
for i in (N[::-1]) :
    dec += int(i) * base
    base *= 2

dec *= 17


binary = 0
base = 1
while dec > 0 :
    last = dec % 2
    binary += last * base
    base*= 10
    dec //= 2

print(binary)
