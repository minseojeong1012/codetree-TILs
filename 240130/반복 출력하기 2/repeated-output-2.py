def print_star(n):    # 1부터 n번째 줄까지 별을 출력하는 함수
    if n == 0:        # n이 0이라면, 더 이상 진행하지 않고
        return        # 퇴각합니다.

    print_star(n - 1) # 1부터 n - 1번째 줄까지 출력하는 함수
    print("HelloWorld")    # n번째 줄에 해당하는 별 출력


n = int(input())
print_star(n)