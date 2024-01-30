def getResult():
    sum_res = 0
    for i in range(a1-1, a2-1 + 1):
        sum_res += arr[i]

    return sum_res

# 입력
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(m):

    # 입력   
    a1, a2 = map(int,input().split())
    
    # 계산 및 출력
    print(getResult())