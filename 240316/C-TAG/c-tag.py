n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(input()))

b = []
for i in range(n):
    b.append(list(input()))

numList = list(range(0, 8))

from itertools import combinations

ans = 0
for num in combinations(numList, 3):
    aSet=set()
    bSet=set()
    for i in range(n):
        atmp = ""
        btmp = ""
        for k in num:
            atmp += a[i][k]
            btmp += b[i][k]
        aSet.add(atmp)
        bSet.add(btmp)
    alen = len(aSet)
    blen = len(bSet)

    if len(aSet | bSet) == alen+blen:
        ans += 1
print(ans)