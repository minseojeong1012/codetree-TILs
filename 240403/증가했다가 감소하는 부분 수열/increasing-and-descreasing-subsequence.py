from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

max_value = 0
for i in range(n): #i 기준으로 꺽임!
    dp = [0 for _ in range(n)]
    #처음을 선택하는 경우 한가지!
    dp[0] = 1

    #dp를 채워감
    for q in range(1, n):
        for j in range(q):
            if base[q] > base[j] and j < i:
                dp[q] = max(dp[q], dp[j]+1)
            if base[q] < base[j] and j >= i:
                dp[q] = max(dp[q], dp[j]+1)
    # print(i, dp)
    max_value = max(max_value, max(dp))
print(max_value)