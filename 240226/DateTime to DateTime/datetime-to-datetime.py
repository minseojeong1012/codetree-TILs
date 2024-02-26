a, b, c = map(int,input().split())
D, H, M, time = 11, 11, 11, 0

#a,b,c 범위 확인
def check():  
    if a > 11:
        return True
    elif a == 11:
        if b > 11:
            return True
        elif b == 11:
            if c >= 11:
                return True
            else:
                return False 
        else:
            return False
    else:
        return False

#시간이 흐름
def tiktok():
    global D, H, M
    M += 1
    if M == 60:
        H += 1
        M = 0
    if H == 24:
        D += 1
        H = 0

#종료 조건
def isTerminate():
    if (D, H, M) == (a, b, c):
        return True
    return False

#실행
if check():
    while not isTerminate():
        tiktok()
        time += 1
    print(time)
else:
    print(-1)