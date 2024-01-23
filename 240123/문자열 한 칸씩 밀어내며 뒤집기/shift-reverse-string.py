n,m = map(str, input().split())

for i in range(int(m)):
    q = int(input())
    if q == 1:
        n = n[1:] + n[0]
        print(n)
    if q == 2:
        n = n[-1] + n[:-1]
        print(n)
    if q == 3:
        n= n[::-1]
        print(n)