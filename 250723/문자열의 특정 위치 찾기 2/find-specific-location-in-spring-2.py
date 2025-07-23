arr = ["apple" , "banana", "grape", "blueberry","orange"]


char = input()
cnt = 0

for i in (arr) :
    if i[2] == char or i[3] == char :
        print(i)
        cnt+=1


print(cnt)
