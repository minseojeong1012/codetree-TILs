MAX_M = 3
MOD = 10007

# 변수 선언 및 입력:
n = int(input())

# dp[i] : 합 i를 만들기 위한 서로 다른 가짓수
dp = [0] * (n + 1)
numbers = [1, 2, 5]
   
# 초기 조건은
# 아직 아무 수도 고르지 않았을 때이므로
# 합 0을 만들기 위한 가짓수가 1이 되어
# dp[0] = 1입니다.
dp[0] = 1

# 점화식에 따라 값을 채워줍니다.
for i in range(1, n + 1):
    # 마지막으로 고른 숫자가 numbers[j]인 경우에 대해
    # 가짓수를 더해줍니다.
    for j in range(MAX_M):
        if i >= numbers[j]:
            dp[i] = (dp[i] + dp[i - numbers[j]]) % MOD

# 합이 n이 되기 위한 가짓수를 출력합니다.
print(dp[n])