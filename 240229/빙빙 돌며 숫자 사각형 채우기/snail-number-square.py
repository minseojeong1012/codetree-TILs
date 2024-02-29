n, m = map(int, input().split())  # 행, 열 개수 입력받기

arr = [  # n 행 m 열 크기의 2차원 배열 정의
    [0 for _ in range(m)]
    for _ in range(n)
]

r, c, d = 0, 0, 0  # 달팽이가 r행 c열에서 d 방향을 바라보고 있다.
dr = [0, 1, 0, -1]  # dr[d] := d 방향으로 이동했을 때 행(row)의 변화량
dc = [1, 0, -1, 0]  # dc[d] := d 방향으로 이동했을 때 열(col)의 변화량
num = 1  # 달팽이가 적어야 하는 수

for _ in range(n * m):  # 달팽이가 모든 칸을 돌아다닐 때까지 반복하라
    # 1. 달팽이가 현재 위치에 수를 적음
    arr[r][c] = num  # r행 c열에 수를 적어줌

    # 2. 이동한다고 치면 도착하는 칸 계산하기
    nr = r + dr[d]
    nc = c + dc[d]

    # 3. 갈 수 있는 지 (격자를 벗어나거나, 이미 수가 적혀있거나)
    # 행, 열이 격자를 벗어나는 경우를 확인
    if nr < 0 or nr >= n or nc < 0 or nc >= m or \
            arr[nr][nc] != 0:  # 이미 수가 적혀있는 경우 확인
        d = (d + 1) % 4  # 시계 방향으로 90도 회전
    
    # 4. 다음으로 갈 격자를 다시 계산
    r = r + dr[d]
    c = c + dc[d]
    num += 1

for i in range(n):
    print(*arr[i])