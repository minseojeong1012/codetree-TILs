A = input()
B = input()
cnt = 0
lenA = len(A)

for i in range(lenA):
    A = A[-1] + A[:-1]
    cnt += 1
    if  A == B:
        break
    if  cnt == lenA:
        print(-1)