# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

cnt = m

# 문제에서 구하고자 하는 값을 반환합니다.
def get_answer():
    global cnt

    return_value = 0
    while cnt:
        return_value += arr[cnt]
        
        if cnt % 2 == 0:
            cnt //= 2
        else:
            cnt -= 1

    return return_value

    
print(get_answer())