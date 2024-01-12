n = 5
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 1. 첫 번째 행에 전부 숫자 1을 채웁니다.
for j in range(n):
    arr_2d[0][j] = 1
for j in range(n):
    arr_2d[j][0]=1

# 2. 두 번째 행부터 마지막 행까지 전부 숫자를 채웁니다.
for i in range(1, n):
    for j in range(1,n):
        arr_2d[i][j] = arr_2d[i - 1][j] + arr_2d[i][j-1]

# 출력
for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()