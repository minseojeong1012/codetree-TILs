# [지금까직 고려한 숫자, 지금까지 숫자를 변경한 횟수, 마지막으로 사용한 숫자]가 정해졌을 때 지금까지 얻은 유사도 값을 최대로 하는 점화식
# dp[i][j][k] = 지금까지 고려한 위치 i, 숫자를 변경한 횟수 j, 마지막에 사용한 숫자가 k 일때 수열의 유사도 최댓값
# 지금까지 고려한 위치가 i 번째로 같고, 숫자를 변경한 횟수는 j 번으로 같고 (j <= m), 마지막에 사용한 숫자가 k로 같으면 유사도는 클수록 좋다 

# 이전에 사용한 숫자 L이 k 와 같은 경우, 다를 경우에 대한 점화식 
# dp[i][j][k] = max(dp[i-1][j][K], dp[i-1][j-1][L]) + x 
# if a[i] == k 이면 x = 1, 아니라면 0


import sys


si = sys.stdin.readline

# n: 1 이상 4이하의 숫자로만 이루어진 길이가 N인 수열 1 <= N <= 500
# m: 순서대로 읽었을 때 인접한 두 숫자가 다른 횟수가 M번 이하 0 <= M <= 100, 최대 숫자 변경 횟수가 M 이하
n, m = map(int, si().split())

arr = list(map(int, si().split()))
dp = [[[0 for _ in range(5)] for _ in range(m + 1)] for _ in range(n)]

# 기저를 구해놓아야 dp 배열을 채울 수 있음
# 한번도 바꾸지 않았을 경우에 대한 케이스도 미리 넣어줄 수 있음
def preprocess():
    # 첫번째로 고른 숫자가 arr의 첫번째 숫자와 같으면 유사도 1
    # m이 0일 경우 고려 
    dp[0][0][arr[0]] = 1

    for i in range(1, n):
        for k in range(1, 5):
            if k == arr[i]:
                dp[i][0][k] = dp[i-1][0][k] + 1
            else:
                dp[i][0][k] = dp[i-1][0][k]


preprocess()
# print(dp)

# m = 0, 즉, 바꿀 기회가 없는 경우 
if m == 0:
    max_result = -sys.maxsize
    for k in range(1, 5):
        max_result = max(max_result, dp[n-1][0][k])
    print(max_result)
    exit(0)

if m != 0:
    # 처음 숫자를 고르는 경우의 수는 기저를 채울때 이미 계산했으므로 1부터
    for i in range(1, n):
        # 한번도 바꾸지 않았을 경우는 기저를 채울때 이미 계산했으므로 1부터 
        for j in range(1, m + 1):
            for k in range(1, 5):
                # 이번에 고른 숫자가 arr[i]와 일치할때 
                if arr[i] == k:
                    # L (이전에 사용한 숫자)를 어떻게 표현하지 
                    # max(이전에 사용한 숫자가 k로 같을 경우, 다를 경우) + 1

                    if k == 1:
                        dp[i][j][k] = max(dp[i-1][j][k], max(dp[i-1][j-1][2], dp[i-1][j-1][3], dp[i-1][j-1][4])) + 1
                    elif k == 2:
                        dp[i][j][k] = max(dp[i-1][j][k], max(dp[i-1][j-1][1], dp[i-1][j-1][3], dp[i-1][j-1][4])) + 1
                    elif k == 3:
                        dp[i][j][k] = max(dp[i-1][j][k], max(dp[i-1][j-1][1], dp[i-1][j-1][2], dp[i-1][j-1][4])) + 1
                    elif k == 4:
                        dp[i][j][k] = max(dp[i-1][j][k], max(dp[i-1][j-1][1], dp[i-1][j-1][2], dp[i-1][j-1][3])) + 1
                        
                else:
                    # max(이전에 사용한 숫자가 k로 같을 경우, 다를 경우)
                    if k == 1:
                        dp[i][j][k] = max(dp[i-1][j][k], max(dp[i-1][j-1][2], dp[i-1][j-1][3], dp[i-1][j-1][4]))
                    elif k == 2:
                        dp[i][j][k] = max(dp[i-1][j][k], max(dp[i-1][j-1][1], dp[i-1][j-1][3], dp[i-1][j-1][4]))
                    elif k == 3:
                        dp[i][j][k] = max(dp[i-1][j][k], max(dp[i-1][j-1][1], dp[i-1][j-1][2], dp[i-1][j-1][4]))
                    elif k == 4:
                        dp[i][j][k] = max(dp[i-1][j][k], max(dp[i-1][j-1][1], dp[i-1][j-1][2], dp[i-1][j-1][3]))


max_result = -sys.maxsize
for j in range(m + 1):
    # 마지막에 고른 숫자가 arr[n]과 같을 경우, 다를 경우 
    for k in range(1, 5):
        max_result = max(max_result, dp[n-1][j][k])

print(max_result)