a = input()
a = list(a)
# Please write your code here.

for i in range(len(a)) :
    if a[i] == '0' :
        a[i] = '1'
        break
    if i == len(a) - 1 :
        a[i] = '0'

x = 0
place = 1
for i in (a[::-1]) :
    x += place * int(i)
    place *= 2

print(x)
