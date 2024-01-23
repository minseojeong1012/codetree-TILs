# 알파벳 소문자를 입력받습니다.
x = input()
	
# 다음 알파벳을 출력합니다.
if x == 'z':
	print("a")
else:
	print(chr(ord(x) + 1))