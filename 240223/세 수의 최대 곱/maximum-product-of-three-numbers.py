from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
base.sort() #오름차순
# print(base)

if 0 in base:
    ans = max(base[0]*base[1]*base[-1], base[-3]*base[-2]*base[-1], 0)
else:
    ans = max(base[0]*base[1]*base[-1], base[-3]*base[-2]*base[-1])
print(ans)