# n을 입력받습니다.
n = int(input())

# 문자열을 구현하고 입력받습니다.
string = [
	input()
	for _ in range(n)
]

# len_all : 전체 문자열의 길이, cnt : 첫번째 문자로 'a'가 나오는 횟수
len_all = 0
cnt = 0
	
# 전체 문자열의 길이와 첫번째 문자로 'a'가 나오는 횟수를 구합니다.
for i in range(n):
	len_all += len(string[i])
	if string[i][0] == 'a':
		cnt += 1
	
# 문제에서 구하고자 하는 값들을 출력합니다.
print(len_all, cnt)