a,b = map(int,input().split())
n1=[]
n2=[]
arr_3 =[[0 for _ in range(b)] for _ in range(a)]
for _ in range(a):
    n1.append(list(map(int,input().split())))

for _ in range(a):
    n2.append(list(map(int,input().split())))
for i in range(a):
    for j in range(b):
        if n1[i][j] == n2[i][j]:
            arr_3[i][j] = 0
        else:
            arr_3[i][j] = 1
for k in range(a):
    for j in range(b):
        print(arr_3[k][j],end=' ')
    print()