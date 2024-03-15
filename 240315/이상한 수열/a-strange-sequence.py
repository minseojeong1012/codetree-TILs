# 변수 선언 및 입력:
n = int(input())


# a번째 수열 값을 반환합니다.
def strange_sequence(a):
    if a == 1:
        return 1
    if a == 2:
        return 2

    return strange_sequence(a // 3) + strange_sequence(a - 1)


print(strange_sequence(n))