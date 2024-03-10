n = int(input())

pigeons = [-1 for _ in range(11)]
cnt = 0

for _ in range(n):
    idx, d = map(int, input().strip().split(" "))
    if pigeons[idx] != -1 and pigeons[idx] != d:
        cnt += 1
    pigeons[idx] = d

print(cnt)