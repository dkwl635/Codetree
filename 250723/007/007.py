secret_code, meeting_point, time = input().split()
time = int(time)

class class_007 :
    def __init__(self, secret_code, meeting_pointm, time) : 
        self.code = secret_code
        self.pointm =  meeting_pointm
        self.time = time

# Please write your code here.
arr  = class_007(secret_code, meeting_point, time)
print(f"secret code : {arr.code}")
print(f"meeting point : {arr.pointm}")
print(f"time : {arr.time}")