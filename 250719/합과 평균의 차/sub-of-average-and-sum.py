# Input
a,b,c = map(int, input().split())
#Add
hop = a + b + c
print(hop)
#Average
average = hop/3
print(f"{average:.0f}")
#Add - Average
print(f"{hop - average:.0f}")