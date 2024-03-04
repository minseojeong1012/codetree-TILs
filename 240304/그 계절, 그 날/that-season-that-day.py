"""
28일: [2월]
29일(윤년): [2월]
30일: [4월, 6월, 9월, 11월]
31일: [1월, 3월, 5월, 7월, 8월, 10월, 12월]
"""
# 계절 확인
def check_season(Y, M, D):
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    fall = [9, 10, 11]
    winter = [12, 1, 2]

    result = isExist(Y, M, D)

    if result:
        if M in spring:
            return "Spring"
        if M in summer:
            return "Summer"
        if M in fall:
            return "Fall"
        if M in winter:
            return "Winter"
    return False

# 윤년 확인
def isLeap(Y):
    if Y % 4 != 0:
        return False
    if Y % 100 != 0:
        return True
    if Y % 400 == 0:
        return True
    return False

# 날짜 존재 확인
def isExist(Y, M, D):
    leap_state = False
    twenty_eight = [28, 2]
    twenty_nine = [29, 2]
    thirty = [30, 4, 6, 9, 11]
    thirty_one = [31, 1, 3, 5, 7, 8, 10, 12]

    leap_state = isLeap(Y)

    if leap_state and M ==2:  # 윤년
        if D > twenty_nine[0]:
            return False
        return True
    elif leap_state == False and M ==2:   # 윤년 x
        if D > twenty_eight[0]:
            return False
        return True
    if M in thirty:
        if D > thirty[0]:
            return False
        return True
    if M in thirty_one:
        return True

Y, M, D = map(int, input().split())
answer = check_season(Y, M, D)

if answer:
    print(answer)
else:
    print(-1)