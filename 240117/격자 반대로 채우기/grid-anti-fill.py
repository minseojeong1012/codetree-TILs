n=int(input())
arr=[
    [0 for _ in range(n)]
    for _ in range(n)
]
num = 1
for j in range(n-1,-1,-1):
    for i in range(n-1,-1,-1):
        if  j %2 == 0:
            arr[i][j] = num+n
            num -= 1
        else:
            arr[i][j] = num
            num += 1

for a in arr:
    for b in a:
        print(b, end=' ')
    print()