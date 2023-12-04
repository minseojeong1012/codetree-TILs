n, m = map(int,input().split())
arr_1 = [list(map(int,input().split())) for _ in range(n)]
arr_2 = [list(map(int,input().split())) for _ in range(n)]
arr_3 = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        if arr_1[i][j] == arr_2[i][j]:
            arr_3[i][j] =0
        else:
            arr_3[i][j] =1

for i in range(n):
    for j in range(m):
        print(arr_3[i][j], end =" ")
    print()