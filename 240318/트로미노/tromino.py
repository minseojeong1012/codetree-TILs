n,m=map(int,input().split())
array=[list(map(int,input().split())) for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]
result=0

# 우, 하, 좌, 상
# dxs=[0,1,0,-1]
# dys=[1,0,-1,0]
# 상, 우, 하
dxs=[-1,0,1]
dys=[0,1,0]

# 블럭이 놓인 칸 안에 적힌 숫자들의 합 구하기 (최댓값)
# 주어진 블럭 회전, 뒤집기 가능
def in_range(x,y):
    if x>=0 and x<n and y>=0 and y<m and not visited[x][y]:
        return True
    return False

def dfs(x,y,turn,cur):
    global result
    global visited

    if turn==2:
        result=max(result,cur)
        return # 빼먹지말기..

    for k in range(3):
        dx=x+dxs[k]
        dy=y+dys[k]

        if in_range(dx,dy):
            cur+=array[dx][dy]
            turn+=1
            visited[dx][dy]=True
            dfs(dx,dy,turn,cur)
            turn-=1
            cur-=array[dx][dy]
            visited[dx][dy]=False
    return 

for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i,j,0,array[i][j])
        visited[i][j]=False

print(result)