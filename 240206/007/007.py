class Place:
    def __init__(self,secret_code,meeting_point,time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

place1 = Place('codetree','L',13)

print("secret code : ",place1.secret_code)
print("meeting point : ",place1.meeting_point)
print("time : ",place1.time)