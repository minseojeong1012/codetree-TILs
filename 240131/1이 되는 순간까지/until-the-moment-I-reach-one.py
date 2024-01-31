def func(N, cnt):
    if N == 1:
        return cnt
    
    if N % 2 == 0:
        N = N // 2
        cnt += 1
        return func(N, cnt)
    else:
        N = N // 3
        cnt += 1
        return func(N, cnt)



n = int(input())
count = func(n, 0)
print(count)