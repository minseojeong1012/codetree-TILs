n , m =map(int,input().split())

num = [[0 for _ in range(m)] for _ in range(n)]

tal = 0
for i in range(m):
    if i%2==0:
        for j in range(n):
            num[j][i] =tal
            tal+=1
    else:
        for j in range(n-1,-1,-1):
            num[j][i]= tal
            tal+=1


for row in num:
    for elem in row:
        print(elem, end=" ")
    print()