n, m, row, col = map(int, input().split())

row, col = row - 1, col - 1

def in_range(row, col):
    return 0 <= row and row < n and 0 <= col and col < n;

# 방향별 좌표값
d_coord_dict = {
    "L": [0, -1],
    "R": [0, 1],
    "U": [-1, 0],
    "D": [1, 0],
}

def str_to_coord(d):
    return d_coord_dict[d]

# 도는 방향을 담은 리스트
d_list = input().split()

# 주사위
dice = [
    [0, 5, 0],
    [4, 6, 3],
    [0, 2, 0]
]

# 현재 주사위눈을 불러오는 함수
def cur_eyes():
    return dice[1][1]

# 주사위를 굴리는 함수
# 규칙
# 1. 세로방향으로 굴리면 세로줄은 변하지만 가로줄은 변하지 않음
# 2. 가로도 동일
# 3. 새로들어오는 주사위눈은 7 - 현재 닿아있는 눈
def roll(d):
    if d == "L":
        dice[1] = [7 - cur_eyes(), dice[1][0], dice[1][1]]
    if d == "R":
        dice[1] = [dice[1][1], dice[1][2], 7 - cur_eyes()]
    if d == "U":
        [dice[0][1], dice[1][1], dice[2][1]] = [7 - cur_eyes(), dice[0][1], dice[1][1]]
    if d == "D":
        [dice[0][1], dice[1][1], dice[2][1]] = [dice[1][1], dice[2][1], 7 - cur_eyes()]

# roll("U")
# print(cur_eyes())

# 격자
grid = [
    [0] * n
    for _ in range(n)
]

# 그리드의 합을 구하는 함수
def sum_grid():
    return sum(map(sum, grid))

# 시작 좌표에 현재 값을 넣어줌 
grid[row][col] = cur_eyes()

# 방향 별로 돌려주며 격자에 숫자 넣어주기
for d in d_list:
    d_row, d_col = d_coord_dict[d]

    # 다음 값으로 들어갈 값을 만들고
    n_row = row + d_row
    n_col = col + d_col

    # 만든 값이 좌표범위 안인지 확인
    # 범위밖이라면 반복문 처음으로 돌아감
    if not in_range(n_row, n_col):
        continue

    # 값을 각각 넣어주고 겨자에도 숫자를 입력
    row = n_row
    col = n_col
    roll(d)
    grid[row][col] = cur_eyes();

# 격자 전체를 더해서 값을 출력
print(sum_grid())