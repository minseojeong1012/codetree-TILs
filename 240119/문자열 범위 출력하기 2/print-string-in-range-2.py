string = input()
n = int(input())

str_len = len(string)
cnt = 0

for i in range(str_len - 2, -1, -1):
	if cnt >= n:
		break
	print(string[i], end="")
	cnt += 1