# 문자열과 q를 입력받습니다.
string, q = input().split()
q = int(q)

# 문자열의 길이를 구합니다.
leng = len(string)

# q개의 질의를 수행합니다.
for _ in range(q):
	# 질의를 입력받습니다.
	quest = input().split()
	
	# 몇번째 질의인지 확인합니다.
	if int(quest[0]) == 1:
		# a번째 문자와 b번째 문자를 교환하여 출력합니다.
		a = int(quest[1])
		b = int(quest[2])
		
		tmp = string[a - 1]
		
		# a번째 문자의 자리에 b번째 문자를 넣습니다.
		string = string[:a - 1] + string[b - 1] + string[a:]
		
		# b번째 문자의 자리에 a번째 문자를 넣습니다.
		string = string[:b - 1] + tmp + string[b:]
		
		# 교환된 문자열을 출력합니다.
		print(string)
	
	else:
		# 문자 a를 전부 b로 변경한 뒤 출력합니다.
		a = quest[1]
		b = quest[2]
	
		# 문자 a를 전부 b로 변경합니다.
		for i in range(leng):
			if string[i] == a:
				string = string[:i] + b + string[i + 1:]
		
		# 변경된 문자열을 출력합니다.
		print(string)