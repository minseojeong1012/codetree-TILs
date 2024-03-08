n = int(input())

def calc(n, cnt):
    if n ==1:
        return cnt
    if n % 2 ==0:
        cnt +=1
        return calc(n//2, cnt)
    else:
        cnt+=1
        return calc(n//3, cnt)

print(calc(n,0))