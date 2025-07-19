#input value
n = int(input())

#n  < 0 -> ice
if n < 0:
    print("ice")
#n > 100 -> water
elif n > 100:
    print("vapor")
#else vapor
else:
    print("water")