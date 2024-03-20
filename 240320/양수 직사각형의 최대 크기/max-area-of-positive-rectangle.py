n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
temp_arr = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            temp_arr[i][j] = 1

def in_range(r,c):
    return 0 <= r and r < n and 0 <= c and c < m

def area(x,y):
    max_area = -1

    for h in range(1,n+1):
        for w in range(1,m+1):
            cnt = count(x, x+h, y, y+w)

            if cnt > max_area:
                max_area = cnt

    return max_area

def count(r1, r2 ,c1, c2):
    total = (r2-r1) * (c2-c1)
    cnt = 0

    for i in range(r1, r2):
        for j in range(c1, c2):
            if in_range(i,j):
                cnt += temp_arr[i][j]

    if cnt == total:
        return cnt
    return -1

max_a = -1
for i in range(n):
    for j in range(m):
        ar = area(i,j)

        if ar > max_a:
            max_a = ar

print(max_a)