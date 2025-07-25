m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

#                 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_A = 0;
for i in range(1, m1) :
    total_A += num_of_days[i]

total_A += d1

total_B = 0;
for i in range(1, m2) :
    total_B += num_of_days[i]

total_B += d2

print(total_B - total_A + 1)