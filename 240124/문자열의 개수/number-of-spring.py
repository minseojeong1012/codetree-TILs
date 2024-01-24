cnt = 0
A = []
while True:
    a = input()
    if  a == '0':
        break
    cnt += 1
    A.append(a)
print(cnt)
for i in range(0,cnt,2):
    print(A[i])