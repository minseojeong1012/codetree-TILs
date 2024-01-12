n=int(input())

MAP=[
[0 for _ in range(n)]
for _ in range(n)
 ]

number=1
for i in range(n):
    for j in range(n):
        MAP[j][i]=number
        number+=1
        #print(MAP[j][i])

# 채워진 배열을 출력합니다.
for row in MAP:
	for elem in row:
		print(elem, end=" ")
	print()