#input value
N = int(input())

# N > 3000 book
if N >= 3000:
    print("book")
# N > 1000 mask
elif N >= 1000:
    print("mask")
# else no
else:
    print("no")