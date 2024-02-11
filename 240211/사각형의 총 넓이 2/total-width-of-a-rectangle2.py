n = int(input())

arr = [
    [0 for _ in range(201)]
    for _ in range(201)
]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    # 음수 좌표를 가급적 다루지 않기 위한 OFFSET 더하기 (Padding 작업)
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100

    # 주어진 직사각형 영역에 대해서 2차원 배열에 표시해주는 작업
    for row in range(x1, x2):
        for col in range(y1, y2):
            arr[row][col] = 1

ans = 0
for row in range(201):
    for col in range(201):
        if arr[row][col] == 1:
            ans += 1

print(ans)