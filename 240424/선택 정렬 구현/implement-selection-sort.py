def sorting(A):
    cnt = len(A)
    tmp = 0
    for i in range(0,cnt):
        minindex = i
        for j in range(i+1,cnt):
            if A[j] < A[minindex]:
                minindex = j
        A[i], A[minindex]= A[minindex], A[i]

    return A



n = int(input())
A = list(map(int,input().split()))
result = sorting(A)
for i in result:
    print(i, end =" ")
#print(result)