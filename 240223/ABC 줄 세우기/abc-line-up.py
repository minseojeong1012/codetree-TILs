from sys import stdin
n = int(stdin.readline())
base = stdin.readline().split()

cnt = 0

#삽입정렬 알고리즘이 효율적일 것
for i in range(1, n): #범위 증가
    for j in range(i, 0, -1): #범위 체크, i~1까지
        if ord(base[j-1]) > ord(base[j]): #작은 게 앞으로
            base[j-1], base[j] = base[j], base[j-1]
            cnt += 1
        else:
            break
# print(base)
print(cnt)