import copy
n=int(input())
array=[list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def bomb(x,y,newArray):
    cnt=array[x][y]
    newArray[x][y]=0
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for i in range(cnt):
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx*i,y+dy*i
            if in_range(nx,ny):
                newArray[nx][ny]=0
    return newArray

def gravity(array):
    tempArr=[[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        temp=n-1
        for i in range(n-1,-1,-1):
            if array[i][j]:
                tempArr[temp][j]=array[i][j]
                temp-=1
    
    return tempArr

def findPair(array):
    dxs,dys=[0,1],[1,0]
    cnt=0
    for x in range(n):
        for y in range(n):
            if array[x][y]==0:
                continue
            for dx,dy in zip(dxs,dys):
                nx,ny=x+dx,y+dy
                if in_range(nx,ny) and array[nx][ny]==array[x][y]:
                    cnt+=1
    return cnt

def simulation():
    result=0
    for i in range(n):
        for j in range(n):
            newArray=copy.deepcopy(array)
            newArray=bomb(i,j,newArray) # 폭탄 터지게 하기
            newArray=gravity(newArray) # 중력 작용
            result=max(result,findPair(newArray)) # 쌍찾기
    return result            

print(simulation())