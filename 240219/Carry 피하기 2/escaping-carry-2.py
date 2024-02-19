N = int(input()) #입력될 숫자의 갯수

numList = [] #입력된 숫자 리스트
numList_digits = []

#입력
for i in range(N):
    temp = int(input())
    numList.append(temp)

#숫자의 자릿수별 리스트 대입
for num in numList:
    digits = []
    for j in range(4):
        digits.append(num % 10)
        num = num // 10
    numList_digits.append(digits)


def is_possible(i, j, k):
    for l in range(4):
        if numList_digits[i][l] + numList_digits[j][l] + numList_digits[k][l] >= 10:
            return False
    
    return True


#각 자리수가 모두 10을 넘지 않는 경우(carry가 발생하지 않는 경우)의 인덱스 찾기
checked_case = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if is_possible(i, j, k):
                checked_case.append([i, j, k])


#위의 경우에 만족하면서 최댓값 찾기
max_Value = 0

for i, j, k in checked_case:
    max_Value = max(max_Value, numList[i] + numList[j] + numList[k])

#경우가 있다면 경우, 없다면 -1 출력
if max_Value:
    print(max_Value)
else:
    print(-1)