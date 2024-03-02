n, m = map(int, input().split())                    # n: 행, m: 열
maze = [[0 for _ in range(m)] for _ in range(n)]    # 채울 숫자 사각형
dirs = ((1,0),(0,1),(-1,0),(0,-1))                  # 하/우/상/좌

r_cnt, c_cnt = n, m-1   # 채울 행과 열의 개수
cur_direction = 0       # 아래 순서부터 시작
x, y = -1,0             # 시작점
num = 0                 # 채우는 수

def write_num():
    global num, x, y, r_cnt, c_cnt
    num += 1            # 숫자 증가
    x, y = x + dirs[cur_direction][0], y + dirs[cur_direction][1]   # 채울 위치
    maze[x][y] = num    # 채우기

while True:
    if num == n*m: break        # 모든 칸을 채웠으면 나가기
    if cur_direction % 2 == 0:              # 하/상의 경우
        for _ in range(r_cnt):              # 채울 행의 개수만큼
            write_num()
        r_cnt -= 1                          # 다음 행에서는 1만큼 감소한 개수만큼 채워야 함
            
    else:                                   # 우/좌의 경우
        for _ in range(c_cnt):              # 채울 열의 개수만큼
            write_num()
        c_cnt -= 1                          # 다음 열에서는 1만큼 감소한 개수만큼 채워야 함
    cur_direction = (cur_direction+1)%4     # 다음 방향은 1 증가
    
for i in range(n):
    for j in range(m):
        print(maze[i][j], end=' ')
    print()