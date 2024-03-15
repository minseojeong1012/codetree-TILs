n = int(input())
arr = list(map(int, input().split()))

def last_common_multiple(n):
    global arr
    
    # 종결 조건
    if n == 1:
        return arr[0]

    lastone = last_common_multiple(n-1)
    
    # 이전 최소공배수와 이번 수와의 최대공약수를 구해 이번 최소 공배수를 구해줌 
    for i in range(arr[n-1], 0, -1):
        if arr[n-1] % i == 0 and lastone % i == 0:
            return lastone // i * arr[n-1] 

        
print(last_common_multiple(n))