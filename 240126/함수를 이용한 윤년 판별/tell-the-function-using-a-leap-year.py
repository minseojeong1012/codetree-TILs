def isYear(y):
    if y % 400 == 0:
        return True
    
    if y % 100 == 0:
        return False

    if y % 4 == 0:
        return True
    
    return False

# 입력
import sys
input = sys.stdin.readline

y = int(input())

# 계산
flag = isYear(y)

# 출력
if flag == True:
    print('true')
else:
    print('false')