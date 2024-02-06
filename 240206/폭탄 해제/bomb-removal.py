class boom:
    def __init__(self,code="",color="",time=0):
        self.cod=code
        self.color=color
        self.time=time


code1,color1,time1=tuple(input().split())

boom1=boom(code1,color1,int(time1))

print(f"code : {boom1.cod}")
print(f"color : {boom1.color}")
print(f"second : {boom1.time}")