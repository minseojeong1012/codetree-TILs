# # 입력
n, k = map(int, input().split())

# 각 칸마다 쌓여있는 블록의 개수
# blocks[i] = i번 칸에 쌓여있는 블록의 개수
# ex. n=7 -> blocks = [0, 0, 0, 0, 0, 0, 0, 0]
blocks = [0 for _ in range(n + 1)]

# k 번 동안 명령을 수행한다.
for _ in range(k):
    # 1. 명령을 입력받기
    # A, B <- 새로운 줄을 입력 받아서 값을 채워주기
    A, B = map(int, input().split())

    # 2. 명령을 수행하기
    # A 부터 B 까지 반복하는 반복문
    for i in range(A, B + 1):
        # i 번 칸에 블록을 하나 추가한다.
        blocks[i] += 1

print(max(blocks))