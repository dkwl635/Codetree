n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
print(*nums, sep=" ")
nums = nums[::-1]
print(*nums, sep=" ")