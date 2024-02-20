from sys import stdin
base = list(map(int, stdin.readline().split()))
base.sort()
# print(base)
result = []
n=6
for i in range(n//2):
    result.append(base[i]+base[-i-1])
result.sort()
print(result[-1]-result[0])