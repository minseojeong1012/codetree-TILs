import sys

si = sys.stdin.readline

R,C = map(int,si().rstrip().split())

grid = [
    si().rstrip().split()
    for _ in range(R)
]

# 같은 색상이 출발,도착지점 일때
# W -> ? -> -> W : 불가능함

# 서로 다른 색상이 출발,도착지점 일 때
# W->B->W->B
# B->W->B->W
result = 0

if grid[0][0] == grid[R-1][C-1]:
    print(result)
else :
    first_gone = []
    sx,sy = 0,0
    for i in range(1,R-1):
        for j in range(1,C-1):
            if grid[sx][sy] != grid[i][j]:
                first_gone.append((i,j))
    for tx,ty in first_gone:
        for i in range(tx+1,R-1):
            for j in range(ty+1,C-1):
                if grid[tx][ty] != grid[i][j]:
                    result+=1
    print(result)