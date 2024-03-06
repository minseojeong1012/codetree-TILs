n = int(input())
OFFSET=1000

class AAA():
    def __init__(self,x,y,no,distance):
        self.x=x
        self.y=y
        self.no=no
        self.distance=distance

aa=[]
for i in range(1,n+1):
    x,y = map(int,input().split())
    # x,y=x+OFFSET,y+OFFSET
    distatnce=abs(x-0)+abs(y-0)
    aa.append(AAA(x,y,i,distatnce))

aa.sort(key=lambda x: x.distance)

for i in range(n):
    print(aa[i].no)
# print(aa)