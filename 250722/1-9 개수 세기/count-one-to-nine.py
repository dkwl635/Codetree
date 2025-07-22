arr = [0] * 9
input_count = input()
input_num = map(int, input().split())

for i in (input_num) :
   arr[i-1] += 1

print(*arr , sep="\n")